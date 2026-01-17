import time
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class QuartoWatcherHandler(FileSystemEventHandler):
    def __init__(self, target_file, watch_dir):
        self.target_file = Path(target_file).resolve()
        self.watch_dir = Path(watch_dir).resolve()
        self.last_triggered = 0
        self.debounce_seconds = 1

    def on_modified(self, event):
        if event.is_directory:
            return

        # 監視対象の拡張子を確認
        if not event.src_path.endswith(".qmd"):
            return

        # 自分自身（target_file）への書き込みによる無限ループを避ける
        if Path(event.src_path).resolve() == self.target_file:
            return

        current_time = time.time()
        if current_time - self.last_triggered > self.debounce_seconds:
            print(
                f"Detected change in {event.src_path}. Touching {self.target_file}..."
            )
            self.touch_target()
            self.last_triggered = current_time

    def touch_target(self):
        # 複数回リトライしてファイルロックに対処する（特にWindows）
        max_retries = 3
        for i in range(max_retries):
            try:
                # 1文字追加して即座に削除することで、内容を変えずにmtimeを更新する
                with open(self.target_file, "a") as f:
                    f.write(" ")

                # Quartoが検知する時間を与える
                time.sleep(0.5)

                with open(self.target_file, "r+") as f:
                    content = f.read()
                    if content.endswith(" "):
                        f.seek(0)
                        f.truncate()
                        f.write(content[:-1])

                print("Successfully touched target file.")
                return
            except Exception as e:
                print(f"Attempt {i + 1} failed to touch target file: {e}")
                time.sleep(0.5)

        print("Failed to touch target file after all retries.")


def main():
    # プロジェクトのルートディレクトリを基準にする
    project_root = Path(__file__).parent.parent.resolve()
    target_qmd = project_root / "quarto" / "textbook.qmd"
    watch_path = project_root / "quarto" / "textbook"

    if not target_qmd.exists():
        print(f"Error: Target file {target_qmd} not found.")
        sys.exit(1)

    print("Starting Quarto Watcher...")
    print(f"Monitoring: {watch_path}")
    print(f"Triggering: {target_qmd}")

    event_handler = QuartoWatcherHandler(target_qmd, watch_path)
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
