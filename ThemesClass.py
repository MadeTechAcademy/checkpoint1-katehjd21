class Theme:
     def __init__(self, name, duty_numbers):
        self.name = name
        self.duty_numbers = duty_numbers
    
     def get_associated_duties(self, all_duties):
        associated_duties = []
        for duty in all_duties:
            split_duty = duty.split(" ", 2)

            if len(split_duty) >= 2 and split_duty[0] == "Duty" and split_duty[1].isdigit():
                duty_number = int(split_duty[1])

                if duty_number in self.duty_numbers:
                    associated_duties.append(duty)
                    
                    
        return associated_duties







        