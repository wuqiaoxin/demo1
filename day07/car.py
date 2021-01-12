class car:
    num=4
    color="宝石蓝"
    brand="BMW A6"
    def run(self):
        print(self.color,"颜色的车有",self.num,"个轮子的车在马路上跑起来了！")
    def push(self):
        print(self.color,"颜色的车拉了50t的货")
c=car()
c.run()
c.push()
c.num=5
c.run()