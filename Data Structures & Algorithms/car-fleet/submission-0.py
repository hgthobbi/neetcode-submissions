class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda car: car[0], reverse = True)
        fleet = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if len(fleet) == 0:
                fleet.append(time)
            elif time > fleet[-1]:
                fleet.append(time)
        return len(fleet)
            
        