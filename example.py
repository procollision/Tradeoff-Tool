import tradeoff_class as tc
#Define paramters in tradeoff
avi = tc.param(name="Availability",weight=1/3,Limitype ="fixed",Limit_val=[1,5])
acc = tc.param(name="Accuracy",weight=1/3,Limitype ="fixed",Limit_val=[1,5])
sam = tc.param(name="sample rate",weight=1/3,Limitype ="fixed",Limit_val=[1,5])
#Define the designs to be traded off source list being the values assigned
gyro = tc.design(name="Gyroscope",sourcelist=[5,3,5])
sun = tc.design(name="Sunsensor",sourcelist=[2,5,3])
star = tc.design(name="Startracker",sourcelist=[3,5,3])
maf = tc.design(name="Magnometer",sourcelist=[5,2,5])
#colors for Latex table generation
colors = [tc.color("EF5350", "red"), tc.color("FB8C00", "orange"), tc.color("FFEB3B", "yellow"), tc.color("8BC34A", "green"), tc.color("00BCD4", "blue")]

tradeoff_att =tc.tradeoff(design_list = [gyro,sun,star,maf],param_list= [avi,acc,sam])

tradeoff_att.get_tradeoff()
tradeoff_att.get_output(language="latex",color_list=colors,width=10,rot="hor",caption="Tradeoff Rotational sensors")





