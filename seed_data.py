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
                continue
            else:
                self.db.put_item(TableName=self.table_name,Item=item)
                print("Item inserted")
            print("--------------")
            print("Total items skipped: "+str(total_skip))
            print("Total items inserted: "+str(total_insert))
def main():
    sd = seed_data()
    sd.seed()
if __name__ == '__main__':
    main()
        
    