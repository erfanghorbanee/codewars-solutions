def update_light(current):
    lights = ["green", "yellow", "red"]
    if current in lights:
        next_index = lights.index(current) + 1
        if next_index > len(lights) - 1:
            next_index = 0

        return lights[next_index]


# https://www.codewars.com/kata/58649884a1659ed6cb000072
