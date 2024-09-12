"""ex01 tea party"""

__author__: str = "730581398"


def main_planner(guests: int) -> None:
    """function main_planner outputs the amount of each item and their total cost given
    the amount of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    """directly use the return value of tea_bags and treats as arguments for cost 
    function"""
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """function tea_bags calculate the amount of teabags needed based on amount of
    people"""
    num_tea_bags: int = people * 2
    return num_tea_bags


def treats(people: int) -> int:
    """function treats calculate the amount of treats needed based on amount of
    people"""
    num_treats: int = int(1.5 * tea_bags(people=people))
    """keyword argument used here"""
    return num_treats


def cost(tea_count: int, treat_count: int) -> float:
    """function cost calculate the total cost of teabags and treats"""
    total_cost: float = 0.5 * tea_count + 0.75 * treat_count
    return total_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
