from inputs import get_gamepad
import SendingMQTT as sending

def main():
    direction = 0
    old_direction = 0
    run = True
    counter = 0
    closing = "Closing"
    while (run == True):
        events = get_gamepad()
        for event in events:
            if (event.ev_type == "Key"):
                if (event.code == "BTN_MODE"):
                    if (event.state == 1):
                        run = False
            if (event.code == "BTN_START"):
                if (event.state == 1):
                    counter += 1
            while (counter%2 != 0):
                events = get_gamepad()
                for event in events:
                    if (event.ev_type == "Key"):
                        if (event.code == "BTN_MODE" and event.state == 1):
                            run = False
                        if (event.code == "BTN_START" and event.state == 1):
                            counter += 1
                        if (event.code == "BTN_TR"):
                            if (event.state == 1):
                                direction = 2
                            else:
                                direction = 0
                        if (event.code == "BTN_TL"):
                            if (event.state == 1):
                                direction = 1
                            else:
                                direction = 0
                    elif (event.ev_type == "Absolute"):
                        if (event.code == "ABS_HAT0X"):
                            if (event.state == 1):
                                direction = 3
                            elif (event.state == -1):
                                direction = 4
                            else:
                                direction = 0
                        else:
                            if (event.state == -1):
                                direction = 2
                            elif (event.state == 1):
                                direction = 1
                            else:
                                direction = 0
                if (old_direction != direction):
                    print ("direction is:\t", direction)
                    sending.main(direction)
                    old_direction = direction
    sending.main(closing)

if __name__ == "__main__":
    main()