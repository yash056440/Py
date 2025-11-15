college = {
    "name": "ABC couputer science",
    "principal_name": "harsh",                               # Create a dictionary 
    "establishment_year": 1998,
    "area": "Mumbai",
    "courses": ["Computer Science"]
}

print(college)                                                # Display 

college["courses"] = ["AI & Data Science"]                    # Update courses name
print("\nAfter updating courses:\n",college)

del college["establishment_year"]                             # Remove  year
print("\nAfter removing establishment year:\n",college)


print("\nFinal College Dictionary:\n",college)                # Final print

