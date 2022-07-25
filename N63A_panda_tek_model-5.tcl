######################################################################################################
#
#						Emre Karagöz
#				    	İstanbul university
#					Astronomy and Space Scienci
#					emrekaragoz1@ogr.iu.edu.tr
#				    	+90 507 515 24 13
######################################################################################################
## Parameters;
######################################################################################################
set name panda-
set n 5
set m 24
set specta _src_grp.pi
set yol -b
set Emin 0.34
set Emax 3.0
set spec ../data/panda/
set tek  tek-m-respect
set nei -nei3.0
######################################################################################################
cd $spec
query yes
method leven
#method simplex
######################################################################################################
setplot energy
setplot add
xset NEIVERS 3.0.4
cpd /xw
setplot command re x 0.4 3.0
setplot command re y 1e-3 0.68
######################################################################################################
for {set i 5} {$i <= $n} {incr i} {
    for {set j 1} {$j <= $m} {incr j} { 
        cd $name$i-$j$yol
        set fileout [open $name$i-$j-$tek$nei.dat a]
        data $name$i-$j$specta
######################################################################################################
	    ignore **-$Emin
	    ignore $Emax-**
	    ignore bad
######################################################################################################
        model (phabs*vphabs*vpshock) & /*
        newpar 1   0.17     	0.01  	1.0E-4  1.0E-4  10     	10    
        newpar 2   0.02     	0.01 	1.0E-4  0       1E+24  	1E+24 
        newpar 3   0.89 	 
        newpar 4   0.303     	
        newpar 5   0.123     
        newpar 6   0.13    	
        newpar 7   0.20     	
        newpar 8   0.30    	
        newpar 9   0.20     	
        newpar 10  0.30     	  
        newpar 11  0.28     	
        newpar 12  0.31     	
        newpar 13  0.31    	
        newpar 14  0.537     	
        newpar 15  0.339     	 
        newpar 16  0.61     	 
        newpar 17  0.15     	 
        newpar 18  0.30     	 
        newpar 19  0.618     	 
        newpar 20  0.30     	0.01  	1.0E-4  1.0E-4  10     	10 
        newpar 21  1.0     	
        newpar 22  0.89     	
        newpar 23  0.303     	
        newpar 24  0.123     	
        newpar 25  0.18     	0.01  	1.0E-4  1.0E-4  10     	10
        newpar 26  0.20     	0.01  	1.0E-4  1.0E-4  10     	10 
        newpar 27  0.20     	0.01  	1.0E-4  1.0E-4  10     	10 
        newpar 28  0.28     	0.01  	1.0E-4  1.0E-4  10     	10 
        newpar 29  0.31     	0.01  	1.0E-4  1.0E-4  10     	10 
        newpar 30  0.537     	
        newpar 31  0.339     	
        newpar 32  0.15     	0.01  	1.0E-4  1.0E-4  10     	10 
        newpar 33  0.618     	
        newpar 34  0.0     	
        newpar 35  1.0E+10      0.01  	1.0E+9  1.0E+9  5e+13   5e+13 
        newpar 36  0.000875     
        newpar 37  1.0     		0.01  	1.0E-5  1.0E-5  10     	10 

        ##data file$i
######################################################################################################
        freeze 1,3-19,21-34,36
        fit
######################################################################################################
	    tclout stat 
	    set chi1 $xspec_tclout
    
	    tclout dof 
	    set dof1 [lindex $xspec_tclout 0]
    
	    setplot command la t Model N63A spectrum: $name$i-$j
	    setplot command la f chi-squared $chi1 / $dof1 dof
    
	    plot ldata del
        cpd $name$i-$j-$tek-1
###################################################################################################
        thaw 25
        fit
        thaw 26
        fit
        thaw 27
        fit
        thaw 28,32
        fit
###################################################################################################
        tclout stat 
        set chi1 $xspec_tclout

        tclout dof 
        set dof1 [lindex $xspec_tclout]

        setplot command la t Model 1 spectrum: $name$i-$j
        setplot command la f chi-squared $chi1 / $dof1 dof

        plot ldata del
        cpd $name$i-$j-$tek-2
###################################################################################################
        tclout stat
        set stat [string trim $xspec_tclout]

        regsub -all { +} $stat { } stat
        set stat [split $stat]

        puts $fileout "$name$i-$j [lindex $stat 0] 			--- chi-square"
#-------------------------------------------------------------------------------------------------
        tclout dof
        set dof [string trim $xspec_tclout]

        regsub -all { +} $dof { } dof
        set dof [split $dof]

        puts $fileout "$name$i-$j [lindex $dof 0] 				--- dof"
#-------------------------------------------------------------------------------------------------
        tclout param 2
        set par2 [string trim $xspec_tclout]

        regsub -all { +} $par2 { } cpar2
        set lpar2 [split $cpar2]

        puts $fileout "$name$i-$j [lindex $lpar2 0] 			--- nH"
#-------------------------------------------------------------------------------------------------
        tclout param 20
        set par20 [string trim $xspec_tclout]

        regsub -all { +} $par20 { } cpar20
        set lpar20 [split $cpar20]

        puts $fileout "$name$i-$j [lindex $lpar20 0] 			--- kT"
#-------------------------------------------------------------------------------------------------
        tclout param 25
        set par25 [string trim $xspec_tclout]

        regsub -all { +} $par25 { } cpar25
        set lpar25 [split $cpar25]

        puts $fileout "$name$i-$j [lindex $lpar25 0] 			--- O"
#-------------------------------------------------------------------------------------------------
        tclout param 26
        set par26 [string trim $xspec_tclout]

        regsub -all { +} $par26 { } cpar26
        set lpar26 [split $cpar26]

        puts $fileout "$name$i-$j [lindex $lpar26 0] 			--- Ne"
#-------------------------------------------------------------------------------------------------
        tclout param 27
        set par27 [string trim $xspec_tclout]

        regsub -all { +} $par27 { } cpar27
        set lpar27 [split $cpar27]

        puts $fileout "$name$i-$j [lindex $lpar27 0] 			--- Mg"
#-------------------------------------------------------------------------------------------------
        tclout param 28
        set par28 [string trim $xspec_tclout]

        regsub -all { +} $par28 { } cpar28
        set lpar28 [split $cpar28]

        puts $fileout "$name$i-$j [lindex $lpar28 0] 			--- Si"
#-------------------------------------------------------------------------------------------------
#        tclout param 29
#        set par29 [string trim $xspec_tcloutt]

#        regsub -all { +} $par29 { } cpar29
#        set lpar29 [split $cpar29]
#
#        puts $fileout "$name$i-$j [lindex $lpar29 0] 			--- S"
#-------------------------------------------------------------------------------------------------
        tclout param 32
        set par32 [string trim $xspec_tclout]

        regsub -all { +} $par32 { } cpar32
        set lpar32 [split $cpar32]

        puts $fileout "$name$i-$j [lindex $lpar32 0] 			--- Fe"
#-------------------------------------------------------------------------------------------------
        tclout param 35
        set par35 [string trim $xspec_tclout]

        regsub -all { +} $par35 { } cpar35
        set lpar35 [split $cpar35]

        puts $fileout "$name$i-$j [lindex $lpar35 0] 			--- Tau_U"
#-------------------------------------------------------------------------------------------------
        tclout param 37
        set par37 [string trim $xspec_tclout]

        regsub -all { +} $par37 { } cpar37
        set lpar37 [split $cpar37]

        puts $fileout "$name$i-$j [lindex $lpar37 0] 			--- Norm \n" 
#################################################################################################
        #parallel error 9
        error max 100 2,20,25-28,32,35,37
#################################################################################################    
        tclout stat
        set stat [string trim $xspec_tclout]

        regsub -all { +} $stat { } stat
        set stat [split $stat]

        puts $fileout "$name$i-$j [lindex $stat 0] 			rerror--- chi-square"
#---------------------------------------------------------------------------------------------------
        tclout dof
        set dof [string trim $xspec_tclout]

        regsub -all { +} $dof { } dof
        set dof [split $dof]

        puts $fileout "$name$i-$j [lindex $dof 0] 			rerror	--- dof"
#---------------------------------------------------------------------------------------------------
        tclout error 2
        set par2 [string trim $xspec_tclout]

        regsub -all { +} $par2 { } cpar2
        set lpar2 [split $cpar2]

        puts $fileout "$name$i-$j [lindex $lpar2 0] 			rerror --- nH - err"
#---------------------------------------------------------------------------------------------------
        tclout error 2
        set par2 [string trim $xspec_tclout]

        regsub -all { +} $par2 { } cpar2
        set lpar2 [split $cpar2]

        puts $fileout "$name$i-$j [lindex $lpar2 1] 	rerror --- nH + err"
#---------------------------------------------------------------------------------------------------
        tclout error 20
        set par20 [string trim $xspec_tclout]

        regsub -all { +} $par20 { } cpar20
        set lpar20 [split $cpar20]

        puts $fileout "$name$i-$j [lindex $lpar20 0] 		rerror --- kT - err"
#---------------------------------------------------------------------------------------------------
        tclout error 20
        set par20 [string trim $xspec_tclout]

        regsub -all { +} $par20 { } cpar20
        set lpar20 [split $cpar20]

        puts $fileout "$name$i-$j [lindex $lpar20 1] 		rerror --- kT + err"
#---------------------------------------------------------------------------------------------------
        tclout error 25
        set par25 [string trim $xspec_tclout]

        regsub -all { +} $par25 { } cpar25
        set lpar25 [split $cpar25]

        puts $fileout "$name$i-$j [lindex $lpar25 0] 	rerror --- O - err"
#---------------------------------------------------------------------------------------------------
        tclout error 25
        set par25 [string trim $xspec_tclout]

        regsub -all { +} $par25 { } cpar25
        set lpar25 [split $cpar25]

        puts $fileout "$name$i-$j [lindex $lpar25 1] 		rerror --- O + err"
#---------------------------------------------------------------------------------------------------
        tclout error 26
        set par26 [string trim $xspec_tclout]

        regsub -all { +} $par26 { } cpar26
        set lpar26 [split $cpar26]

        puts $fileout "$name$i-$j [lindex $lpar26 0] 		rerror --- Ne - err"
#---------------------------------------------------------------------------------------------------
        tclout error 26
        set par26 [string trim $xspec_tclout]

        regsub -all { +} $par26 { } cpar26
        set lpar26 [split $cpar26]

        puts $fileout "$name$i-$j [lindex $lpar26 1] 		rerror --- Ne + err"
#---------------------------------------------------------------------------------------------------
        tclout error 27
        set par27 [string trim $xspec_tclout]

        regsub -all { +} $par27 { } cpar27
        set lpar27 [split $cpar27]

        puts $fileout "$name$i-$j [lindex $lpar27 0] 		rerror --- Mg - err"
#---------------------------------------------------------------------------------------------------
        tclout error 27
        set par27 [string trim $xspec_tclout]

        regsub -all { +} $par27 { } cpar27
        set lpar27 [split $cpar27]

        puts $fileout "$name$i-$j [lindex $lpar27 1] 		rerror --- Mg + err"
#---------------------------------------------------------------------------------------------------
        tclout error 28
        set par28 [string trim $xspec_tclout]

        regsub -all { +} $par28 { } cpar28
        set lpar28 [split $cpar28]

        puts $fileout "$name$i-$j [lindex $lpar28 0] 		rerror --- Si - err"
#---------------------------------------------------------------------------------------------------
        tclout error 28
        set par28 [string trim $xspec_tclout]

        regsub -all { +} $par28 { } cpar28
        set lpar28 [split $cpar28]

        puts $fileout "$name$i-$j [lindex $lpar28 1] 		rerror --- Si + err"
#---------------------------------------------------------------------------------------------------
        #tclout error 29
        #set par29 [string trim $xspec_tclout]

        #regsub -all { +} $par29 { } cpar29
        #set lpar29 [split $cpar29]

        #puts $fileout "$name$i-$j [lindex $lpar29 0] 		rerror --- S - err"
#---------------------------------------------------------------------------------------------------
        #tclout error 29
        #set par29 [string trim $xspec_tclout]

        #regsub -all { +} $par29 { } cpar29
        #set lpar29 [split $cpar29]

        #puts $fileout "$name$i-$j [lindex $lpar29 1] 		rerror --- S + err"
#---------------------------------------------------------------------------------------------------
        tclout error 32
        set par32 [string trim $xspec_tclout]

        regsub -all { +} $par32 { } cpar32
        set lpar32 [split $cpar32]

        puts $fileout "$name$i-$j [lindex $lpar32 0] 		rerror --- Fe - err"
#---------------------------------------------------------------------------------------------------
        tclout error 32
        set par32 [string trim $xspec_tclout]

        regsub -all { +} $par32 { } cpar32
        set lpar32 [split $cpar32]

        puts $fileout "$name$i-$j [lindex $lpar32 1] 		rerror --- Fe + err"
#---------------------------------------------------------------------------------------------------
        tclout error 35
        set par35 [string trim $xspec_tclout]

        regsub -all { +} $par35 { } cpar35
        set lpar35 [split $cpar35]

        puts $fileout "$name$i-$j [lindex $lpar35 0] 	rerror --- Tau_u - err"
#---------------------------------------------------------------------------------------------------
        tclout error 35
        set par35 [string trim $xspec_tclout]

        regsub -all { +} $par35 { } cpar35
        set lpar35 [split $cpar35]

        puts $fileout "$name$i-$j [lindex $lpar35 1] 	rerror --- Tau_u + err"
#---------------------------------------------------------------------------------------------------
        tclout error 37
        set par37 [string trim $xspec_tclout]

        regsub -all { +} $par37 { } cpar37
        set lpar37 [split $cpar37]

        puts $fileout "$name$i-$j [lindex $lpar37 0] 	rerror --- Norm - err"
#---------------------------------------------------------------------------------------------------
        tclout error 37
        set par37 [string trim $xspec_tclout]

        regsub -all { +} $par37 { } cpar37
        set lpar37 [split $cpar37]

        puts $fileout "$name$i-$j [lindex $lpar37 1] 	rerror --- Norm + err \n"
#####################################################################################################    
        tclout stat 
        set chi1 $xspec_tclout
        tclout dof 
        set dof1 [lindex $xspec_tclout 0]

        setplot command la t Model 1 spectrum: $name$i-$j
        setplot command la f chi-squared $chi1 / $dof1 dof

        plot ldata del
        cpd  $name$i-$j-$tek-3
######################################################################################################
#	cpd /xw
#        plot ldat del
#        iplot
###################################################################################################### 
        data none
        model none
        close $fileout
        cd ../
######################################################################################################    
    }
}

exit

"""
color 12 on 2
lwitdh 4.5 on 2
lwidth 4.5 on 1
lwidth 4.5 on 3
lwidth 4.5
csize 1.3
time off
LAbel 3 VP 0.80 0.84 "C16" csize 2
label pos y 2.5
la T
la F
plot

hardcopy C16.png/cps
quit

setplot command re x 0.34 3.0
setplot command re y 1e-3 0.28
"""
