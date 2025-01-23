#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
# 

# some clarifying questions to ask for this one
# 1. Are the identifiers fixed or they can vary
# 2. If there is a single character in the log is it still considered as a digit log

# @lc code=start
class LogManager:
    def __init__(self) -> None:
        self.digit_logs = defaultdict(list)
        self.letter_logs = defaultdict(list)
        self.res = []
    
    def _arrange_logs(self):
        # arrange letter logs first
        if len(self.letter_logs):
            log_dump = sorted([[identifier, content[0]] for identifier, content in self.letter_logs.items()],  key= lambda x: (x[1], x[0]))            
            for identifier, content in log_dump:
                self.res.append(identifier + " " + content)
                

        if len(self.digit_logs):
            log_dump = [[identifier, content[0]] for identifier, content in self.digit_logs.items()]
            for identifier, content in log_dump:
                self.res.append(identifier + " " + content)

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logManager = LogManager()

        # process logs
        for log in logs:
            tokens = log.split(" ")
            identifier, contents = tokens[0], tokens[1:]

            digitLog = True
            for i, content in enumerate(contents):
                if content == ' ':
                    continue
                elif not content.isdigit():
                    digitLog = False
                    break
            
            if digitLog:
                logManager.digit_logs[identifier].append(" ".join(contents))
            else:
                logManager.letter_logs[identifier].append(" ".join(contents))
        
        print(logManager.digit_logs)
        print(logManager.letter_logs)
        
        logManager._arrange_logs()
        return logManager.res
        
# @lc code=end