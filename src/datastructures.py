"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""


class FamilyStructure:
    def __init__(self, last_name: str):
        self.last_name = last_name
        self._next_id = 1
        self._members = []
        self.add_member({
            'first_Name': 'Jhon',
            'Age': 33,
            'Lucky_number': [7, 13, 22]
        })
        self.add_member({
            'First_name': 'Jane',
            'Age': 35,
            'Lucky_numbers': [10, 14, 3]
        })
        self.add_member({
            'First_name': 'Jimmy',
            'Age': 5,
            'Lucky_numbers': [5]
        })

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if 'id' not in member or member['id'] is None:
            member['id'] = self._generate_id()
        else:
            if member['id'] >= self._next_id:
                self._next_id = member['id'] + 1
        member['Last Name'] = self.last_name
        self._members.append(member)

    pass

    def delete_member(self, id):
        for i, memb in enumerate(self.members):
            if memb.get('id') == id:
                self._members.pop(i)
                return True
        return False
            
    pass

    def get_member(self, id):
        for memb in self._members:
            if memb.get('id') == id:
                return memb
        return None

    pass

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
