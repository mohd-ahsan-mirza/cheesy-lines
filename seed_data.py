import boto3
class seed_data:
    def __init__(self):
        self.table_name = 'cheesy_lines'
        self.db =  boto3.client('dynamodb')
        self.partition_key = 'dateadded'
        self.sort_key = 'line_number'
        self.__data = [
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"1"},'sent':{"N":"0"},"line":{"S":"You’re So Cute It’s Distracting"}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"2"},'sent':{"N":"0"},'line':{"S":"You’re So Hot You Would Make The Devil Sweat"}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"3"},'sent':{"N":"0"},'line':{"S":"On a scale of 1 to 10, you’re a 9 and I’m the 1 you lack"}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"4"},'sent':{"N":"0"},'line':{"S":"Are you a magician? Because whenever I look at you, everyone else disappears!"}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"5"},'sent':{"N":"0"},'line':{"S":"They say Disneyland is the happiest place on earth. Well apparently, no one has ever been standing next to you."}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"6"},'sent':{"N":"0"},'line':{"S":"Was your dad a boxer? Because damn, you’re a knockout!"}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"7"},'sent':{"N":"0"},'line':{"S":"There’s only one thing I want to change about you, and that’s your last name."}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"8"},'sent':{"N":"0"},'line':{"S":"Are you a dictionary? Cause you’re adding meaning to my life."}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"9"},'sent':{"N":"0"},'line':{"S":"Are you a magician? Because whenever I look at you, everyone else disappears!"}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"10"},'sent':{"N":"0"},"line":{"S":"Are you a camera? Because every time I look at you, I smile."}},
            {self.partition_key:{"N":"20190601"},self.sort_key: {"N":"11"},'sent':{"N":"0"},'line':{"S":"Do you work at Starbucks? Because I like you a latte."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"12"},'sent':{"N":"0"},'line':{"S":"If you were a burger at McDonald’s you’d be the McGorgeous."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"13"},'sent':{"N":"0"},'line':{"S":"I love your face. Is it McDonalds?"}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"14"},'sent':{"N":"0"},'line':{"S":"You would be the McGorgeous if you were a burger at McDonalds."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"15"},'sent':{"N":"0"},'line':{"S":"This is love at first site, which is as spicy as McDonalds’ chili sauce."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"16"},'sent':{"N":"0"},'line':{"S":"Both you and McDonalds make my heart stop."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"17"},'sent':{"N":"0"},'line':{"S":"You stole my heart. You must be the Hamburglar."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"18"},'sent':{"N":"0"},'line':{"S":"If you were in McDonalds menu, you’d be McBeautiful."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"19"},'sent':{"N":"0"},'line':{"S":"You are almost as delightful as this Egg White Delight."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"20"},'sent':{"N":"0"},'line':{"S":"If you were a meal at McDonalds, you would be a mchottie."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"21"},'sent':{"N":"0"},'line':{"S":"If you were a chicken to be served at McDonalds, you would be mcchicken."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"22"},'sent':{"N":"0"},'line':{"S":"Like at McDonalds I like to see you smile."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"23"},'sent':{"N":"0"},'line':{"S":"This could be love at first bite."}},
            {self.partition_key:{"N":"20190615"},self.sort_key: {"N":"24"},'sent':{"N":"0"},'line':{"S":"Like chicken nuggets entrance my taste buds, you captivate my heart."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"1"},'sent':{"N":"0"},'line':{"S":"Hi, I'm writing a book on the finer things of life and I was wondering if I could interview you?"}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"2"},'sent':{"N":"0"},'line':{"S":"You are the reason that men fall in love."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"3"},'sent':{"N":"0"},'line':{"S":"If you were a tear drop I would never cry for fear of losing you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"4"},'sent':{"N":"0"},'line':{"S":"Are you as beautiful on the inside as you are on the outside?"}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"5"},'sent':{"N":"0"},'line':{"S":"Why would I want to look at the stars when I can look in your eyes?"}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"6"},'sent':{"N":"0"},'line':{"S":"I just want you to know that when I picture myself happy, it's with you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"7"},'sent':{"N":"0"},'line':{"S":"They say honesty is the best policy, so I have to tell you that you're the most beautiful woman I have ever seen."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"8"},'sent':{"N":"0"},'line':{"S":"Are you a tower? Because Eiffel for you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"9"},'sent':{"N":"0"},'line':{"S":"Even if there was no gravity, I'd still fall for you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"10"},'sent':{"N":"0"},'line':{"S":"Baby, you're so sweet you put Hershey's out of business."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"11"},'sent':{"N":"0"},'line':{"S":"Your daddy must be a drug dealer, because you're dope."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"12"},'sent':{"N":"0"},'line':{"S":"What are you doing for the rest of your life? Because I want to spend it with you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"13"},'sent':{"N":"0"},'line':{"S":"You're hotter than the bottom of my laptop."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"14"},'sent':{"N":"0"},'line':{"S":"I would flirt with you, but I'd rather seduce you with my awkwardness."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"15"},'sent':{"N":"0"},'line':{"S":"You must be a keyboard, because you're just my type."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"16"},'sent':{"N":"0"},'line':{"S":"You're so hot, if you ate bread you'd poop out toast."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"17"},'sent':{"N":"0"},'line':{"S":"Did you get your licenses suspended for driving all these guys crazy?"}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"18"},'sent':{"N":"0"},'line':{"S":"You're hot, I'm ugly. Let's make average babies."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"19"},'sent':{"N":"0"},'line':{"S":"You're so hot, you must be the reason for global warming."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"20"},'sent':{"N":"0"},'line':{"S":"Are you a banana, because I find you so a-peel-ing?"}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"21"},'sent':{"N":"0"},'line':{"S":"You're so sweet you're giving me a toothache."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"22"},'sent':{"N":"0"},'line':{"S":"You wanna know the best thing in my life? It's the first word of this sentence."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"23"},'sent':{"N":"0"},'line':{"S":"You're pretty and I'm cute. Together we'd be pretty cute."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"24"},'sent':{"N":"0"},'line':{"S":"You're like a dictionary. You add meaning to my life."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"25"},'sent':{"N":"0"},'line':{"S":"If you hold 8 roses in front of a mirror, you'll see 9 of the most beautiful things in the world."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"26"},'sent':{"N":"0"},'line':{"S":"You are so beautiful that you give the sun a reason to shine."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"27"},'sent':{"N":"0"},'line':{"S":"This morning I saw a flower and I thought it was the most beautiful thing I have ever seen; until I met you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"28"},'sent':{"N":"0"},'line':{"S":"Are you an interior decorator? Because when I saw you the room became beautiful."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"29"},'sent':{"N":"0"},'line':{"S":"We must be near an airport because my heart just took off when I saw you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"30"},'sent':{"N":"0"},'line':{"S":"You are absolutely, astoundingly gorgeous, and that’s the least interesting thing about you."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"31"},'sent':{"N":"0"},'line':{"S":"s your name Ariel? Because we mermaid for each other."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"32"},'sent':{"N":"0"},'line':{"S":"Your eyes are like IKEA...I get lost in them."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"33"},'sent':{"N":"0"},'line':{"S":"You must be Jamaican, because Jamaican me crazy."}},
            {self.partition_key:{"N":"20190630"},self.sort_key: {"N":"34"},'sent':{"N":"0"},'line':{"S":"If you were a steak you would be well done."}},
        ]
    def item_exists(self,key):
            item = self.db.get_item(TableName=self.table_name,Key=key)
            if "Item" in item:
                return True
            else:
                return False
    def seed(self):
        total_insert = 0
        total_skip = 0
        for item in self.__data:
            print(item)
            if self.item_exists({self.partition_key:item[self.partition_key],self.sort_key:item[self.sort_key]}):
                print("Item exists...Skipping")
                total_skip = total_skip + 1
                continue
            else:
                self.db.put_item(TableName=self.table_name,Item=item)
                print("Item inserted")
                total_insert = total_insert + 1
            print("--------------")
            print("Total items skipped: "+str(total_skip))
            print("Total items inserted: "+str(total_insert))
def main():
    sd = seed_data()
    sd.seed()
if __name__ == '__main__':
    main()
        
    