import logging
import os
import sys
from datetime import datetime

class UpdateBuildNumber:
    curr_time = ""
    ERROR_CODE = 1
    SUCCESS_CODE = 0
    now = datetime.now()
    
    def __init__(self, logging_level=None):
        """Initialize logger and logging level\n
        :param logging_level: Level of logging to be used, default: WARNING
        """
        FORMAT = '[%(levelname)-8s %(name)-10s %(asctime)-15s] %(message)s'
        logging.basicConfig(format=FORMAT)
        self.log_it = logging.getLogger(__name__)
        self.log_it.setLevel(logging.INFO)
    
    def Update_build_number(self):
        """Update time in txt file
        :prints: curr_time
        """
        file_name = "Text_file_1"
        try:
            f = open(file_name, "w")
            f. truncate()
            curr_time = self.now.strftime("%H:%M:%S")
            f.write("Time: ")
            f.write(curr_time)
            f.close()
            print("successfull updated time")
            print(curr_time)
            return True
        except KeyError:
            self.log_it.warning("Couldnt update time")
            return False

    def main(self):
        """Main routine of the Update_Build_Number index
        """
        if (not self.Update_build_number()):
            self.log_it.error("Couldnt update time in file")
            return self.ERROR_CODE               
        return self.SUCCESS_CODE

if __name__ == '__main__':
    Update_Build_Number = UpdateBuildNumber()
    sys.exit(Update_Build_Number.main())
