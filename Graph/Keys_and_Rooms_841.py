class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited_room = set()

        def dfs(room):
            visited_room.add(room)
            keys = rooms[room]
            for key in keys:
                if key not in visited_room:
                    dfs(key)

        dfs(0)
        return len(visited_room) == len(rooms)


rooms = [[1], [2], [3], []]
rooms = [[1, 3], [3, 0, 1], [2], [0]]
sol = Solution()
print(sol.canVisitAllRooms(rooms))
