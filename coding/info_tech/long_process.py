#@title Interrupting Execution of long running processes

#@markdown Long running python processes can be interrupted. Run the following cell and select **Runtime -> Interrupt execution** (*hotkey: Cmd/Ctrl-M I*) to stop execution.

#@markdown Press ▶ and then cancel this process!

#@markdown
import time
print("Running long process...")
time.sleep(30) # sleep for a while; interrupt me!
print("Done Sleeping")
