from pathlib import Path
import re

ROOT = Path(
    "/Users/jermainehardy/Library/CloudStorage/"
    "SynologyDrive-Media/Anime/Naruto"
)

DRY_RUN = True

SEASON_RANGES = {
    1: (1, 57),
    2: (58, 100),
    3: (101, 141),
    4: (142, 183),
    5: (184, 220),
}

VIDEO_EXTENSIONS = {".mkv", ".mp4", ".avi", ".m4v"}

pattern = re.compile(
    r"^\[Anime Time\]\s*Naruto\s*-\s*(\d{3})\s*-\s*(.*)$",
    re.IGNORECASE,
)


def get_season_info(absolute_episode):
    for season, (first_episode, last_episode) in SEASON_RANGES.items():
        if first_episode <= absolute_episode <= last_episode:
            season_episode = absolute_episode - first_episode + 1
            return season, season_episode

    return None


def clean_title(title):
    return title.strip().strip(" -")


def main():
    planned_changes = []
    skipped = []
    errors = []

    # Search all season folders, except Season 00.
    season_folders = sorted(ROOT.glob("Season [0-9][0-9]"))

    for current_folder in season_folders:
        if current_folder.name == "Season 00":
            print("SKIPPING SPECIALS: Season 00")
            continue

        for file_path in current_folder.iterdir():
            if not file_path.is_file():
                continue

            if file_path.suffix.lower() not in VIDEO_EXTENSIONS:
                continue

            match = pattern.match(file_path.stem)

            if not match:
                skipped.append(file_path)
                continue

            absolute_episode = int(match.group(1))
            title = clean_title(match.group(2))

            season_info = get_season_info(absolute_episode)

            if season_info is None:
                errors.append(
                    f"Episode {absolute_episode:03d} is outside 001-500: "
                    f"{file_path}"
                )
                continue

            season_number, season_episode = season_info

            correct_folder = ROOT / f"Season {season_number:02d}"

            if title:
                new_name = (
                    f" Naruto - "
                    f"S{season_number:02d}E{season_episode:02d} - "
                    f"{title}{file_path.suffix}"
                )
            else:
                new_name = (
                    f" Naruto - "
                    f"S{season_number:02d}E{season_episode:02d}"
                    f"{file_path.suffix}"
                )

            destination = correct_folder / new_name

            planned_changes.append(
                (file_path, correct_folder, destination)
            )

    # Check for duplicate destinations BEFORE changing anything.
    destinations = {}

    for source, folder, destination in planned_changes:
        if destination in destinations:
            errors.append(
                "DUPLICATE DESTINATION:\n"
                f"  {destinations[destination]}\n"
                f"  {source}\n"
                f"  -> {destination}"
            )
        else:
            destinations[destination] = source

    if errors:
        print("\n" + "=" * 70)
        print("ERRORS FOUND - NOTHING WILL BE CHANGED")
        print("=" * 70)

        for error in errors:
            print(error)
            print()

        return

    move_count = 0
    rename_only_count = 0

    for source, correct_folder, destination in planned_changes:

        needs_move = source.parent != correct_folder

        print()
        print(f"FROM: {source}")

        if needs_move:
            print(f"MOVE TO: {correct_folder}")

        print(f"FINAL: {destination.name}")

        if needs_move:
            move_count += 1
        else:
            rename_only_count += 1

        if not DRY_RUN:
            correct_folder.mkdir(parents=True, exist_ok=True)

            if destination.exists() and destination != source:
                print("ERROR: Destination already exists.")
                print(destination)
                continue

            source.rename(destination)

    print()
    print("=" * 70)

    if DRY_RUN:
        print("DRY RUN COMPLETE")
        print("NO FILES WERE MOVED OR RENAMED.")
    else:
        print("COMPLETE")

    print(f"Files needing move + rename: {move_count}")
    print(f"Files needing rename only: {rename_only_count}")
    print(f"Total planned files: {len(planned_changes)}")
    print(f"Skipped files: {len(skipped)}")

    if skipped:
        print()
        print("SKIPPED FILES:")
        for file_path in skipped:
            print(f"  {file_path}")


if __name__ == "__main__":
    main()