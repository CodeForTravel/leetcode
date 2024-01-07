# from collections import deque


# class Solution(object):
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
#         queue = deque()
#         for ch in senate:
#             queue.append(ch)
#         v_r = 0
#         v_d = 0

#         while queue:
#             current = queue.popleft()
#             if current == "R":
#                 v_r += 1
#                 if queue and queue[0] == "D":
#                     queue.popleft()
#                 elif v_d > 0:
#                     v_d -= 1
#             elif current == "D":
#                 v_d += 1
#                 if queue and queue[0] == "R":
#                     queue.popleft()
#                 elif v_r > 0:
#                     v_r -= 1
#         return "Dire" if v_d > v_r else "Radiant"

from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r_queue = deque()
        d_queue = deque()
        for i, ch in enumerate(senate):
            if ch == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            r_value = r_queue.popleft()
            d_value = d_queue.popleft()

            if r_value < d_value:
                r_queue.append(r_value + len(senate))
            else:
                d_queue.append(d_value + len(senate))

        return "Radiant" if r_queue else "Dire"


senate = "RRRDDR"
senate = "RD"
senate = "RDD"
senate = "DDDRRD"
senate = "DDRRR"


sol = Solution()
print(sol.predictPartyVictory(senate))
