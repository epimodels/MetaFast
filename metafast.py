import random

# Intervention File Functions

def IntHeader(file,year):
	headstring = "InterventionVersion = " + str(year)
	file.write(headstring + "\n")
	
def IntSubpop(id,name,dir,file):
	file.write("\n")
	file.write("SubpopulationId = " + str(id) + "\n")
	file.write("SubpopulationName = " + "\"" + str(name) + "\"" + "\n")
	file.write("SubpopulationFile = " + str(dir) + "\n")

def IntAction(file,id,desc,delay,duration,type,efficacy=False):
	file.write("\n")
	file.write("ActionId = " + str(id) + "\n")
	file.write("ActionDescription = " + str(desc) + "\n")
	file.write("ActionDelay = " + str(delay) + "\n")
	file.write("ActionDuration = " + str(duration) + "\n")
	file.write("ActionType = " + str(type) + "\n")
	if efficacy == False:
		return 0
	else:
		file.write("ActionEfficacy = " + str(efficacy) + "\n")

def Intervention(file,id,startdate,members,mutex,compliance,action,enddate=False,state=False):
	file.write("\n")
	file.write("InterventionId = " + str(id) +"\n")
	file.write("InterventionType = Offline" + "\n")
	if enddate == False:
	    file.write("ConditionDate = " + str(startdate) + "~" + str(startdate)+ "\n")
	else:
	    file.write("ConditionDate = " + str(startdate) + "~" + str(enddate)+ "\n")
	file.write("ConditionMembership = " + str(members) + "\n")
	if mutex == False:
		pass
	else:
		file.write("ConditionMutex = " + str(mutex) + "\n")
	file.write("ConditionCompliance = " + str(compliance) + "\n")
	file.write("Action = " + str(action) + "\n")
	if state == False:
	    pass
	else:
	    file.write("ConditionState = " + str(state) + "\n")
	
# Configuration File Functions

def ConfigDisease(file,trans,seednum,asymp,asympf,seedtype="default",incfile="default",incformat="default", inffile="default",infformat="default"):
    file.write("Transmissibility = " + str(trans) + "\n")
    if incformat == "default":
        file.write("IncubationPeriodFormat = DISTRIBUTION" + "\n")
    else:
        file.write("IncubationPeriodFormat = " + str(incformat) + "\n")
    if incfile == "default":
        file.write("IncubationPeriodFile = cfg/Incubation.Period.Distribution" + "\n")
    else:
        file.write("IncubationPeriodFile = " + str(incfile) + "\n")
        
    if infformat == "default":
        file.write("InfectiousPeriodFormat = DISTRIBUTION" + "\n")
    else:
        file.write("InfectiousPeriodFormat = " + str(infformat) + "\n")
    if inffile == "default":
        file.write("InfectiousPeriodFile = cfg/Infectious.Period.Distribution" + "\n")
    else:
        file.write("InfectiousPeriodFile = " + str(inffile) + "\n")
    
    if seedtype == "default":
        file.write("EpidemicSeedType = RANDOM_SEEDS_EVERY_DAY" + "\n")
    else:
        file.write("EpidemicSeedType = " + str(seedtype) + "\n")
    file.write("DailySeedNumber = " + str(seednum) + "\n")
    file.write("AsymptomaticProbability = " + str(asymp) + "\n")
    file.write("AsymptomaticFactor = " + str(asympf) + "\n")

def ConfigAdmin(file,gfile,outfile,logfile,intervention,diagnosis,duration,iterations,propnum,gformat="default",outlevel=2010,seed="default",version=2009):
    if gformat == "default":
        file.write("ContactGraphFileFormat = EFIG6Bb" + "\n")
    else:
        file.write("ContactGraphFileFormat = " + str(gformat) + "\n")
    file.write("ContactGraphFile = " + str(gfile) + "\n")
    if outlevel == 2010:
        file.write("OutputLevel = 2010" + "\n")
    else:
        file.write("OutputLevel = " + str(outlevel) + "\n")
    file.write("OutputFile = " + str(outfile) + "\n")
    file.write("LogFile = " + str(logfile) + "\n")
    file.write("SimulationDuration = " + str(duration) + "\n")
    file.write("IterationNumber = " + str(iterations) + "\n")
    file.write("PropagationNumber = " + str(propnum) + "\n")
    if seed == "default":
        file.write("SimulationRandomSeed = " + str(random.random()) + "\n")
    else:
        file.write("SimulationRandomSeed = " + str(seed) + "\n")
    if version == 2009:
        file.write("ConfigVersion = 2009" + "\n")
    else:
        file.write("ConfigVersion = " + str(version) + "\n")
    file.write("InterventionFile = " + str(intervention) + "\n")
    file.write("Diagnosis = " + str(diagnosis) + "\n")

# qsub File Functions
def qsubMake(file,nodes,ppn,group,dir,name,configname,logname,convert="default",epifast="default"):
    workdir = str(dir)
    file.write("#!/bin/bash" + "\n")
    file.write("\n")
    file.write("#PBS -l walltime=6:00:00" + "\n")
    file.write("#PBS -l nodes=" +str(nodes) + ":" + "ppn=" + str(ppn) + "\n")
    file.write("#PBS -W group_list=" + str(group) + "\n")
    file.write("#PBS -N " + str(name) + "\n")
    file.write("#PBS -q " + str(group) + "_q" + "\n")
    file.write("#PBS -A " + str(group) + "\n")
    file.write("#PBS -j oe" + "\n")
    file.write("#PBS -o "+ workdir + "out" + "\n")
    file.write("\n")
    file.write("NUM_NODES=`/bin/cat $PBS_NODEFILE | /usr/bin/wc -l | /bin/sed \"s/ //g\"`" + "\n")
    file.write("MPIRUN=\"mpiexec_mpt -n $NUM_NODES" + "\"" + "\n")
    file.write("\n")
    if epifast == "default":
        file.write("EpiFast=/vbi/projects/EpiFast/bin/EpiFast" + "\n")
    else:
        file.write("EpiFast=" + str(epifast)+"\n")
    if convert == "default":
        file.write("Convert5to6Program=/vbi/projects/EpiFast/bin/Convert.EFIG5.To.EFIG6Bb" + "\n")
    else:
        file.write("Convert5to6Program=" + str(convert) + "\n")
    file.write("\n")
    file.write("WORKDIR=" + workdir + "\n")
    file.write("INPUTDIR=${WORKDIR}/input" + "\n")
    file.write("OUTPUTDIR=${WORKDIR}/out" + "\n")
    file.write("LOGDIR=${WORKDIR}/log" + "\n")
    file.write("MPI_BUFS_PER_PROC=512" + "\n")
    file.write("MPI_BUFS_PER_HOST=1024" + "\n")
    file.write("\n")
    file.write("cd ${WORKDIR}" + "\n")
    file.write("$MPIRUN ${EpiFast} ${WORKDIR}/" + str(configname) + " > ${LOGDIR}/" + str(logname) + "\n")
    file.write("\n")
    file.write("exit;")
