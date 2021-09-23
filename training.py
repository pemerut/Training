art_friend = {"Rolf", "Anne", "Jen"}
science_friend = {"Jen", "Charlie"}

art_but_not_science = art_friend.difference(science_friend)
science_but_not_art = science_friend.difference(art_friend)

not_in_both = art_friend.symmetric_difference(science_friend)

art_and_science = art_friend.intersection(science_friend)

all_friends = art_friend.union(science_friend)
print(all_friends)