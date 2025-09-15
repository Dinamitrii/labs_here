from alive_progress import alive_bar

import speedtest_here


# actual func here
def compute():
    with alive_bar(1000) as bar:  # your expected total
        for item in speedtest_here.main():        # the original loop
            print(item)           # your actual processing here
            bar()                 # call `bar()` at the end


compute()
