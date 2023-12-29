from config import folders, scripts


def run_script(folder, script):
    try:
        module = __import__(f"{folder}.{script}", fromlist=["run"])
        getattr(module, "run")()
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Exception caught: {type(e).__name__} - {e}")
        print("Script not found or does not contain a 'run' function.")


def main():
    print("Available folders:")
    for key, value in folders.items():
        print(f"{key}. {value}")

    folder_choice = input("Enter folder number: ")
    folder = folders.get(folder_choice)

    print(f"Available scripts in {folder}:")
    for key, value in scripts.items():
        print(f"{key}. {value}")

    script_choice = input("Enter script number: ")
    script = scripts.get(script_choice)

    run_script(folder, script)


if __name__ == "__main__":
    main()
