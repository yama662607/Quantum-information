// Read chapter times from the same metadata generated with each MP4.
document.addEventListener("DOMContentLoaded", () => {
  const requests = new Map();
  for (const video of document.querySelectorAll("video")) {
    const source = video.querySelector("source");
    if (!source || !source.src.includes("/assets/videos/ep")) continue;
    const url = source.src.replace(/\.mp4(?:\?.*)?$/, ".lesson.json");
    if (!requests.has(url)) {
      requests.set(url, fetch(url).then(response => {
        if (!response.ok) throw new Error(`Chapter metadata: ${response.status}`);
        return response.json();
      }));
    }
    requests.get(url).then(lesson => {
      const nav = document.createElement("nav");
      nav.className = "quantum-video-chapters";
      nav.setAttribute("aria-label", `${lesson.title}のチャプター`);
      nav.style.cssText = "display:flex;flex-wrap:wrap;gap:0.4rem;margin-top:0.7rem";
      for (const chapter of lesson.chapters) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "btn btn-sm btn-outline-light";
        button.style.cssText = "text-align:left;white-space:normal";
        const seconds = Math.floor(chapter.start);
        const time = `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, "0")}`;
        button.textContent = `${time} ${chapter.title}`;
        button.addEventListener("click", () => {
          video.currentTime = chapter.start;
          video.pause(); // Give the reader time to predict before resuming.
          video.focus();
        });
        nav.append(button);
      }
      const duration = document.createElement("span");
      duration.style.cssText = "width:100%;color:#cbd5e1;font-size:0.85rem";
      duration.textContent = `全長 ${Math.floor(lesson.duration / 60)}分${Math.round(lesson.duration % 60)}秒。章を選ぶと一時停止した状態で移動します。`;
      nav.prepend(duration);
      video.after(nav);
    }).catch(error => console.warn("Video chapters could not be loaded", error));
  }
});
