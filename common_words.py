def find_common_words(*lists):
    # Convert all lists to sets for fast intersection
    set_lists = [set(l) for l in lists]
    # Find the intersection of all sets
    common_words = set.intersection(*set_lists)
    # Return the common words as a list
    return list(common_words)
  
  
