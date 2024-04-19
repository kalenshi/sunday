def get_users() -> dict[str, str]:
	users: dict[str, str] = {
		"1": "Jeff", "2": "Bob", "3": "Patience", "4": "Robert"
	}
	return users


def two_sums(nums: list[int], target: int) -> list[int]:
	seen = {}
	for i in range(len(nums)):
		if target - nums[i] in seen:
			return [seen[target - nums[i]], i]
		else:
			seen[nums[i]] = i
	return []


if __name__ == "__main__":
	print(two_sums([2, 7, 11, 15], 9))
	print(two_sums([2, 3, 4], 6))
	print(two_sums([3, 3], 6))
