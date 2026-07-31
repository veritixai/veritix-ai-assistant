def split_script_into_scenes(script):

    lines = []

    for line in script.split("\n"):

        line = line.strip()

        if line:
            lines.append(line)

    return lines