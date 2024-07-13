from scripts.create_snapshot import create_snapshots
from scripts.manage_snapshot import manage_snapshots

def main():
    create_snapshots()
    manage_snapshots()

if __name__ == "__main__":
    main()