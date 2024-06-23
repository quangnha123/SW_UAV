import os

def run_commands():
    # Danh sách các lệnh cần chạy
    commands = ["./PX4-Autopilot/Tools/simulation/gazebo-classic/sitl_multiple_run.sh -n 6 -m iris",
        ".local/lib/python3.10/site-packages/mavsdk/bin/mavsdk_server udp://:14541 -p 50060",
        ".local/lib/python3.10/site-packages/mavsdk/bin/mavsdk_server udp://:14542 -p 50061",
        ".local/lib/python3.10/site-packages/mavsdk/bin/mavsdk_server udp://:14543 -p 50062",
        ".local/lib/python3.10/site-packages/mavsdk/bin/mavsdk_server udp://:14544 -p 50063",
        ".local/lib/python3.10/site-packages/mavsdk/bin/mavsdk_server udp://:14545 -p 50064",
        ".local/lib/python3.10/site-packages/mavsdk/bin/mavsdk_server udp://:14546 -p 50065",
        "./QGroundControl.AppImage",
        "cd new8 && python3 main.py"]

    # Mở 7 terminal độc lập và chạy từng lệnh trên mỗi terminal
    for command in commands:
        os.system(f"gnome-terminal -- /bin/bash -c '{command}; exec /bin/bash' &")

if __name__ == "__main__":
    run_commands()
