# Quarto Best Practices for Technical Textbooks

This guide summarizes the research on Quarto best practices, specifically optimized for mathematical and scientific textbook projects like "Quantum Information".

## 1. Project Navigation & Structure

### Sidebar & Chapter Numbering
*   **Unnumbered Index**: The home page (`index.qmd`) should usually be unnumbered to act as a Preface.
    ```markdown
    # Preface {.unnumbered}
    ```
*   **Part-based Organization**: Use `part` in `_quarto.yml` to group multiple chapters.
    ```yaml
    book:
      chapters:
        - index.qmd
        - part: "Mathematical Background"
          chapters:
            - chapter1.qmd
            - chapter2.qmd
    ```
*   **Controlled Numbering**: Enable global section numbering and set the depth.
    ```yaml
    number-sections: true
    number-depth: 3
    ```

### Modular Content (`include`)
*   **Hybrid Approach**: Use a wrapper `.qmd` file that includes partial files (`_*.qmd`).
*   **Expansion**: The `{{< include >}}` shortcode is expanded before Pandoc filters run, meaning cross-references in included files work seamlessly.
*   **Recursive Includes**: Quarto supports recursive includes (e.g., A includes B, B includes C) but will error on circular dependencies.

---

## 2. Technical Authoring

### Cross-References
*   **Chapter-based Numbering**: For technical books, ensure figures and equations are numbered by chapter (e.g., Fig 1.2).
    ```yaml
    crossref:
      chapters: true
    ```
*   **Labels**: Use `#sec-`, `#fig-`, `#eq-` prefixes for automatic detection and localized labels.

### Japanese Localization (`lang: ja`)
*   **Automatic Translations**: Setting `lang: ja` in `_quarto.yml` automatically translates key terms:
    - Figure -> 図
    - Table -> 表
    - Appendix -> 付録
*   **Typography**: For PDF output, ensure Unicode support for Japanese characters.
    ```yaml
    format:
      pdf:
        mainfont: "Hiragino Sans GB" # OS-dependent
        CJKmainfont: "IPAexGothic"  # For LaTeX
    ```

### SCSS & Theme Customization
*   **Layered Defaults**: Quarto uses a layered SCSS compilation. Define variables in the `/*-- scss:defaults --*/` section of your SCSS file.
*   **Variable Precedence**: User-defined variables override Quarto and Bootstrap defaults if defined with `!default` or placed correctly in the sequence.
*   **Bootstrap Integration**: Use `$theme-colors` and other Bootstrap variables to maintain consistency.

---

## 3. Advanced Authoring & Optimization

### Math Rendering (KaTeX vs MathJax)
*   **KaTeX (Recommended for Books)**: Faster rendering, especially for documents with many equations.
    ```yaml
    format:
      html:
        html-math-method: katex
    ```
*   **MathJax**: More feature-rich (supports more complex LaTeX extensions) but slower. Use if KaTeX fails for specific complex notation.
*   **Global Macros**: While KaTeX macros are not directly in `_quarto.yml`, you can include a hidden math block with `\gdef` in a common included file.

### Bibliographies & Citations
*   **Global Bibliography**: Define `bibliography` in `_quarto.yml` for project-wide access.
*   **Inclusion boundaries**: Quarto's Citeproc system indexes citations across `{{< include >}}` boundaries, ensuring a unified reference list.
*   **Citation Styles**: Use `.csl` files to strictly follow specific academic standards (e.g., IEEE, Nature).

---

### LaTeX & Mathematical Packages
*   **Custom Preamble**: Use `include-in-header: preamble.tex` to include advanced packages like `physics` or `braket`.
    ```yaml
    format:
      pdf:
        include-in-header: preamble.tex
    ```
*   **Theorems & Cross-refs**: Use Quarto's built-in theorem environment for consistent numbering across formats. Combine with `crossref: chapters: true` for technical precision.

### Visuals & Code Optimization
*   **Mermaid Format**: For non-HTML formats (PDF/DOCX), explicitly set `mermaid-format: svg` or `png` to ensure high-quality rendering.
*   **Code Freeze**: Enable `execute: freeze: auto` at the project level to avoid unnecessary re-computation in large books.
*   **Python (Qiskit/Research)**: Ensure your environment (e.g., `QUARTO_PYTHON`) points to a kernel containing your specific research libraries.

---

## 5. Summary & Project Recommendations
*   **Navigation**: Use the "Hybrid" wrapper model for the best balance of modularity and maintainability.
*   **Automation**: Integrate `just check` into development and potentially CI/CD.
*   **Localization**: Leverage `lang: ja` for most needs, and `_language.yml` for specific branding overrides.
