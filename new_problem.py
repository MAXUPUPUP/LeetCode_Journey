import argparse
import re
from pathlib import Path


LANG_TO_EXT = {
    "python": "py",
    "cpp": "cpp",
    "java": "java",
}


def slugify(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "untitled"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a LeetCode solution file from template."
    )
    parser.add_argument("--id", required=True, help="Problem id, e.g. 1 or 121")
    parser.add_argument("--title", required=True, help='Problem title, e.g. "Two Sum"')
    parser.add_argument(
        "--lang",
        required=True,
        choices=["python", "cpp", "java"],
        help="Language: python/cpp/java",
    )
    parser.add_argument(
        "--topic",
        default="array/hash-table/dp/...",
        help="Topic label shown in file header",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite file if it already exists",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    problem_id = str(int(args.id)).zfill(4)
    slug = slugify(args.title)
    ext = LANG_TO_EXT[args.lang]

    template_path = root / "templates" / f"problem_template.{ext}"
    output_dir = root / "solutions" / args.lang
    output_path = output_dir / f"{problem_id}_{slug}.{ext}"

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    if output_path.exists() and not args.force:
        raise FileExistsError(
            f"File already exists: {output_path}\nUse --force to overwrite."
        )

    content = template_path.read_text(encoding="utf-8")
    content = (
        content.replace("{id}", str(int(args.id)))
        .replace("{title}", args.title.strip())
        .replace("{slug}", slug.replace("_", "-"))
        .replace("{array/hash-table/dp/...}", args.topic.strip())
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()

