import commands
import csv

config_file = 'config.txt'

def runCommand(cmd):

    status, output = commands.getstatusoutput(cmd)
    return status, output

def showPackages():

    cmd = "mgmt_cli show packages -r true"
    #status, output = commands.getstatusoutput(cmd)
    #print (status)
    #print (output)
    #os.system(cmd)
    status, output = runCommand(cmd)
    print (status)
    print (output)

def showPackage(package_name):

    cmd = "mgmt_cli show package name %s -r true" % (package_name)
    #status, output = commands.getstatusoutput(cmd)
    #print (status)
    #print (output)
    #os.system(cmd)
    status, output = runCommand(cmd)
    print (status)
    print (output)


def verifyPolicy(policy_name):
    
    cmd = "mgmt_cli verify-policy policy-package %s -r true" % (policy_name)
    #status,
    status, output = runCommand(cmd)
    # print (status)
    # print (output)

    return status, output

def installPolicy(policy_name, targets):

    # targets is a list

    if not targets:
        cmd = "mgmt_cli install-policy policy-package %s -r true" % (policy_name)
    else:
        print ("Targets are specified")
        print (targets)

        i = 1
        for tar in targets:
            if i == 1:
                targets = "targets.1 " + tar
                i = i + 1
            else:
                targets = targets + " targets." + str(i) + " " + tar
                i = i + 1

        cmd = "mgmt_cli install-policy policy-package %s %s -r true" % (policy_name, targets)
     
        #gateways = ''.join(targets)
        #print(gateways)
        #cmd = "mgmt_cli install-policy policy-package %s targets %s -r true" % (policy_name, gateways)
        #print(cmd)
    print (cmd)
    
    status, output = runCommand(cmd)
    return status, output


def readConfig():

    installme = []

    with open(config_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # avoid comment line
            if '#' not in row[0]:
                print (row)
                installme.append(row)
                print installme

    return installme

def batchVerify(policies):


    for policy in policies:
        print("Verifying %s") % (policy[0])
        status, output = verifyPolicy(policy[0])
        if status != 0:
            print (status)
            print (output)
            print ("Problem with verifying %s policy. Stopping..") % (policy[0])
            exit()

    return 0

def batchInstallPolicy(policies):

    print (policies)

    for policy in policies:

        if len(policy) > 1:
            # targets specified
            print ("Installing policy on these gateways: %s") % (policy[1:])
            targets = policy[1:]
        else:
            print("Target gateways for %s is specified") % (policy[0])
            targets = None


        print("Installing %s..") % (policy[0])

        status, output = installPolicy(policy[0], targets)

        print (status)
        print (output)

        if status != 0:
            print ("Problem installing %s policy. Moving on to next..") % (policy[0])



def main():

    gateways = [ "test-gw-2", "test-cluster-1"]

    #showPackages()
    #showPackage("HomelabPolicy")
    #showPackage("BoyPolicy")
    #installPolicy("HomelabPolicy", [])
    #installPolicy("AWSNCAPolicy", gateways)
    print ("Hello!")
    tasks = readConfig()
    

   # if 0 == batchVerify(tasks):
    batchInstallPolicy(tasks)


if __name__ == '__main__':
    main()