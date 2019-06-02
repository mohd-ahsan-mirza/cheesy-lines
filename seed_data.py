import boto3
class seed_data:
    def __init__(self):
        self.db =  boto3.client('dynamodb')
        self.__data = [
            {'line_number': {"N":"1"},'sent':{"N":"0"},"line":{"S":"You’re So Cute It’s Distracting"}},
            {'line_number': {"N":"2"},'sent':{"N":"0"},"line":{"S":"You’re So Hot You Would Make The Devil Sweat"}},
            {'line_number': {"N":"3"},'sent':{"N":"0"},"line":{"S":"On a scale of 1 to 10, you’re a 9 and I’m the 1 you lack"}},
            {'line_number': {"N":"4"},'sent':{"N":"0"},"line":{"S":"Are you a magician? Because whenever I look at you, everyone else disappears!"}},
            {'line_number': {"N":"5"},'sent':{"N":"0"},"line":{"S":"They say Disneyland is the happiest place on earth. Well apparently, no one has ever been standing next to you."}},
            {'line_number': {"N":"6"},'sent':{"N":"0"},"line":{"S":"Was your dad a boxer? Because damn, you’re a knockout!"}},
            {'line_number': {"N":"7"},'sent':{"N":"0"},"line":{"S":"There’s only one thing I want to change about you, and that’s your last name."}},
            {'line_number': {"N":"8"},'sent':{"N":"0"},"line":{"S":"Are you a dictionary? Cause you’re adding meaning to my life."}},
        ]
    def seed(self):
        for item in self.__data:
            print(item)
            self.db.put_item(TableName='cheesy_lines',Item=item)
def main():
    sd = seed_data()
    sd.seed()
if __name__ == '__main__':
    main()
        
    