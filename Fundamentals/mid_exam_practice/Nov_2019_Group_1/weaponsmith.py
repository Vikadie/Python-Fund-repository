weapon_particles = input().split("|")

commands = input()

while commands != 'Done':
    commands = commands.split()
    if commands[0] == "Move":
        index = int(commands[2])
        if commands[1] == "Left":
            if 0 < index < len(weapon_particles):
                weapon_particles[index - 1], weapon_particles[index] = weapon_particles[index], weapon_particles[index - 1]
        else:
            if 0 <= index < len(weapon_particles) - 1:
                weapon_particles[index], weapon_particles[index + 1] = weapon_particles[index + 1], weapon_particles[
                    index]
    elif commands[0] == "Check":
        check_list = []
        if commands[1] == "Even":
            for i in range(0, len(weapon_particles), 2):
                check_list.append(weapon_particles[i])
        else:
            for i in range(1, len(weapon_particles), 2):
                check_list.append(weapon_particles[i])
        print(' '.join(check_list))

    commands = input()


print(f"You crafted {''.join(weapon_particles)}!")