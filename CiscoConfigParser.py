from ciscoconfparse import CiscoConfParse

class ParseSomeCisco:

    def __init__(self, file):
        self.file = file

    def ParseIt(self):
        parse = CiscoConfParse([
            '!',
            'interface Serial1/0',
            ' ip address 1.1.1.5 255.255.255.252'
            ])
        #for obj in parse.find_objects(r"interface"):
            #print("Object: ", obj)
            #print("Config text: ", obj.text)


        #Supposed to find a parent based on Child criteria
        #serial_objs = parseExample.find_objects("^interface Serial")
        #for obj in serial_objs:
            #print("Object: ", obj)
            #print("Text: ", obj.text, "\n")

        #List iteration of above method
        all_intfs = parseExample.find_objects("^interf")
        qos_intfs = [obj for obj in self.file.find_objects(r"^interf")
                     if obj.re_search_children(r"service-policy output QOS_1")]
        #print(qos_intfs)

        config = ['!',
                  'interface FastEthernet0/1',
                  ' switchport access vlan 532',
                  ' spanning-tree vlan 532 cost 3',
                  '!',
                  'interface FastEthernet0/2',
                  ' switchport access vlan 300',
                  ' spanning-tree portfast',
                  '!',
                  'interface FastEthernet0/3',
                  ' duplex full',
                  ' speed 100',
                  ' switchport access vlan 300',
                  ' spanning-tree portfast',
                  '!',
            ]
        p = CiscoConfParse(config)
        #print(p.find_objects_w_child('^interface',
                                     #'switchport access vlan 300'))

        #Lists each Object without specified child
        #if not bool(parseExample.find_objects(r'no cdp run')):
            #cdps_intfs = parseExample.find_objects_wo_child(r'^interface',
                                                            #r'no cdp enable')
        #print(cdps_intfs)

        return qos_intfs

    def printTheParse(self, parsed):
        return parsed


parseExample = CiscoConfParse([
        '!',
        'policy-map QOS_1',
        ' class GOLD',
        '  priority percent 10',
        ' class SILVER',
        '  bandwidth 30',
        '  random-detect',
        ' class default',
        '!',
        'interface Ethernet0/0',
        ' ip address 1.1.2.1 255.255.255.0',
        ' no cdp enable',
        '!',
        'interface Serial1/0',
        ' encapsulation ppp',
        ' ip address 1.1.1.1 255.255.255.252',
        '!',
        'interface Serial1/1',
        ' encapsulation ppp',
        ' ip address 1.1.1.5 255.255.255.252',
        ' service-policy output QOS_1',
        '!',
        'interface Serial1/2',
        ' encapsulation hdlc',
        ' ip address 1.1.1.9 255.255.255.252',
        '!',
        'class-map GOLD',
        ' match access-group 102',
        'class-map SILVER',
        ' match protocol tcp',
        '!',
        ])

info = ParseSomeCisco(parseExample)
gotit = info.ParseIt()
printIt = info.printTheParse(gotit)
print(printIt)