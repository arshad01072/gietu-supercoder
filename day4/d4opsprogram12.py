class table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=table()
back_table=table()
front_table=back_table
back_table=dining_table
print(id(dining_table),id(back_table),id(front_table))

        
