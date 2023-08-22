Problem Link -> https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

def JobScheduling(self,jobs,n):
        
        # code here
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)


        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0


        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break


        return countJobs, jobProfit
