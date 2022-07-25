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
set n 3
set m 1
set l 9
set k 2
set Emin 0.34
set Emax 3.0
set name panda
set specta _src_grp.pi
set dpng  _tek-m-png
set loop -freeze53-semi
set spec ../data/
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
#set fileout [open emre_result.dat a]
for {set i 3} {$i <= $n} {incr i} {
    for {set j 9} {$j <= $l} {incr j} {
		for {set z 2} {$z <= $k} {incr z} {
			set fileout [open $i-$m-$j-$z-$name$loop.dat a]
			data $name$i-$m-$j-$z$specta
######################################################################################################
			ignore **-$Emin
			ignore $Emax-**
			ignore bad
######################################################################################################
			model (phabs*vphabs*(vpshock+vpshock)) & /*
			newpar 1   0.17     	0.01  	1.0E-4  1.0E-4  10     	10    
			newpar 2   0.03	    	0.01 	1.0E-4  0       1E+24  	1E+24 
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
			newpar 20  0.57     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 21  1.0     	
			newpar 22  0.89     	
			newpar 23  0.303     	
			newpar 24  0.123     	
			newpar 25  0.14     	0.01  	1.0E-4  1.0E-4  10     	10
			newpar 26  0.26     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 27  0.24     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 28  0.40     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 29  0.31     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 30  0.537     	
			newpar 31  0.339     	
			newpar 32  0.13     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 33  0.618     	
			newpar 34  0.0     	
			newpar 35  1.3E+11    	0.01  	1.0E+9  1.0E+9  5e+13   5e+13 
			newpar 36  0.000875     
			newpar 37  1.0     		0.01  	1.0E-5  1.0E-5  10     	10 
			newpar 38  0.50     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 39  1.0     	
			newpar 40  0.89     	
			newpar 41  0.303     	
			newpar 42  0.123     	
			newpar 43  0.13     	0.01  	1.0E-4  1.0E-4  10     	10
			newpar 44  0.20     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 45  0.20     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 46  0.28     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 47  0.31     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 48  0.537     	
			newpar 49  0.339     	
			newpar 50  0.15     	0.01  	1.0E-4  1.0E-4  10     	10 
			newpar 51  0.618     	
			newpar 52  0.0     	
			newpar 53  1.0E+10   	0.01  	1.0E+9  1.0E+9  5e+13   5e+13 
			newpar 54  0.000875     
			newpar 55  1.0     		0.01  	1.0E-5  1.0E-5  10     	10 
			##data file$i
###################################################################################################
			freeze 1-36,39-54
			freeze 20
			fit
###################################################################################################
			tclout stat 
			set chi1 $xspec_tclout
			tclout dof 
			set dof1 [lindex $xspec_tclout 0]

			setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
			setplot command la f chi-squared $chi1 / $dof1 dof

			plot ldata del
			cpd $name$i-$m-$j-$z-a$loop
###################################################################################################
			fit
			thaw 43,53
			fit
#----------------------------------------------------------------------------------------------------
            tclout param 53
            set param53 [lindex $xspec_tclout 0]
            if {$param53 >= 2.5E+12} {
                    newpar 53 2.5E+12
                    nepawr 55 1.0
                    freeze 53
                    puts "Param53 (Tau_u) frozen now"
                    thaw 2,43-46,50
                    fit
                    freeze 2,37,38,43-46,50,55
                    thaw 53
                    fit
#----------------------------------------------------------------------------------------------------
                    plot ldata del
                    tclout stat
                    set chi1 $xspec_tclout
                    tclout dof 
                    set dof1 [lindex $xspec_tclout 0]

                    setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
                    setplot command la f chi-squared $chi1 / $dof1 dof
                            

                    cpd $name$i-$m-$j-$z-b$loop
#----------------------------------------------------------------------------------------
                    tclout stat
                    set stat [string trim $xspec_tclout]

                    regsub -all { +} $stat { } stat
                    set stat [split $stat]

                    puts $fileout "$i-$m-$j-$z [lindex $stat 0] 			---high53-chi-square"
#----------------------------------------------------------------------------------------		
                    tclout dof
                    set dof [string trim $xspec_tclout]

                    regsub -all { +} $dof { } dof
                    set dof [split $dof]
                    
                    puts $fileout "$i-$m-$j-$z  [lindex $dof 0] 				---high53-dof"
#----------------------------------------------------------------------------------------		
                    tclout param 2
                    set par2 [string trim $xspec_tclout]

                    regsub -all { +} $par2 { } cpar2
                    set lpar2 [split $cpar2]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar2 0] 			---high53-ism-nH"
#----------------------------------------------------------------------------------------		
                    tclout param 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 0] 			---high53-ism-norm"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 0] 			---high53-kT"
#--------------------------------------------------------------------------------------------------------
                    tclout param 43
                    set par43 [string trim $xspec_tclout]

                    regsub -all { +} $par43 { } cpar43
                    set lpar43 [split $cpar43]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar43 0] 			---high53-O"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 44
                    set par44 [string trim $xspec_tclout]

                    regsub -all { +} $par44 { } cpar44
                    set lpar44 [split $cpar44]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar44 0] 			---high53-Ne"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 45
                    set par45 [string trim $xspec_tclout]

                    regsub -all { +} $par45 { } cpar45
                    set lpar45 [split $cpar45]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar45 0] 			---high53-Mg"
#--------------------------------------------------------------------------------------------------------	
                    tclout param 46
                    set par46 [string trim $xspec_tclout]

                    regsub -all { +} $par46 { } cpar46
                    set lpar46 [split $cpar46]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar46 0] 			---high53-Si"
#--------------------------------------------------------------------------------------------------------	
                    tclout param 47
                    set par47 [string trim $xspec_tclout]

                    regsub -all { +} $par47 { } cpar47
                    set lpar47 [split $cpar47]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar47 0] 			---high53-S"
#--------------------------------------------------------------------------------------------------------	
                    tclout param 50
                    set par50 [string trim $xspec_tclout]

                    regsub -all { +} $par50 { } cpar50
                    set lpar50 [split $cpar50]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar50 0] 			---high53-Fe"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 53
                    set par53 [string trim $xspec_tclout]

                    regsub -all { +} $par53 { } cpar53
                    set lpar53 [split $cpar53]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar53 0] 			---high53-Tau_u"
#-----------------------------------------------------------------------------------------------------	
                    tclout param 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 0] 			---high53-ejekta-norm \n" 
#-----------------------------------------------------------------------------------------------------	
                    parallel error 1
                    error max 50 53
#-----------------------------------------------------------------------------------------------------
                    tclout stat 
                    set chi1 $xspec_tclout
                    tclout dof 
                    set dof1 [lindex $xspec_tclout 0]

                    setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
                    setplot command la f chi-squared $chi1 / $dof1 dof

                    plot ldata del
                    cpd $name$i-$m-$j-$z-c$loop
#----------------------------------------------------------------------------------------				
                    tclout stat
                    set stat [string trim $xspec_tclout]

                    regsub -all { +} $stat { } stat
                    set stat [split $stat]

                    puts $fileout "$i-$m-$j-$z  [lindex $stat 0] 			---high53-rerror-chi-square"
#----------------------------------------------------------------------------------------		                   
                    tclout error 53
                    set par53 [string trim $xspec_tclout]

                    regsub -all { +} $par53 { } cpar53
                    set lpar53 [split $cpar53]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar53 0] 			---high53-rerror-Tau_u-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 53
                    set par53 [string trim $xspec_tclout]

                    regsub -all { +} $par53 { } cpar53
                    set lpar53 [split $cpar53]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar53 1] 			---high53-rerror-Tau_u+err\n"
#--------------------------------------------------------------------------------------------------------	                    
                    thaw 2,37,38,43-46,50,55
                    freeze 53
                    fit
#--------------------------------------------------------------------------------------------------------                    
                    parallel error 9
                    error max 50 2,37,38,43-46,50,55
#----------------------------------------------------------------------------------------
                    tclout error 2
                    set par2 [string trim $xspec_tclout]

                    regsub -all { +} $par2 { } cpar2
                    set lpar2 [split $cpar2]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar2 0] 			---high53-rerror-ism-nH-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 2
                    set par2 [string trim $xspec_tclout]

                    regsub -all { +} $par2 { } cpar2
                    set lpar2 [split $cpar2]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar2 1] 			---high53-rerror-ism-nH+err"
#--------------------------------------------------------------------------------------------------------
                    tclout error 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 0] 			---high53-rerror-ism-norm-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 1] 			---high53-rerror-ism-norm+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 0] 			---high53-rerror-kT-err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 1] 			---high53-rerror-kT+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 43
                    set par43 [string trim $xspec_tclout]

                    regsub -all { +} $par43 { } cpar43
                    set lpar43 [split $cpar43]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar43 0] 			---high53-rerror-O-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 43
                    set par43 [string trim $xspec_tclout]

                    regsub -all { +} $par43 { } cpar43
                    set lpar43 [split $cpar43]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar43 1] 			---high53-rerror-O+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 44
                    set par44 [string trim $xspec_tclout]

                    regsub -all { +} $par44 { } cpar44
                    set lpar44 [split $cpar44]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar44 0] 			---high53-rerror-Ne-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 44
                    set par44 [string trim $xspec_tclout]

                    regsub -all { +} $par44 { } cpar44
                    set lpar44 [split $cpar44]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar44 1] 			---high53-rerror-Ne+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 45
                    set par45 [string trim $xspec_tclout]

                    regsub -all { +} $par45 { } cpar45
                    set lpar45 [split $cpar45]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar45 0] 			---high53-rerror-Mg-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 45
                    set par45 [string trim $xspec_tclout]

                    regsub -all { +} $par45 { } cpar45
                    set lpar45 [split $cpar45]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar45 1] 			---high53-rerror-Mg+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 46
                    set par46 [string trim $xspec_tclout]

                    regsub -all { +} $par46 { } cpar46
                    set lpar46 [split $cpar46]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar46 0] 			---high53-rerror-Si-err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 46
                    set par46 [string trim $xspec_tclout]

                    regsub -all { +} $par46 { } cpar46
                    set lpar46 [split $cpar46]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar46 1] 			---high53-rerror-Si+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 47
                    set par47 [string trim $xspec_tclout]

                    regsub -all { +} $par47 { } cpar47
                    set lpar47 [split $cpar47]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar47 0] 			---high53-rerror-S-err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 47
                    set par47 [string trim $xspec_tclout]

                    regsub -all { +} $par47 { } cpar47
                    set lpar47 [split $cpar47]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar47 1] 			---high53-rerror-S+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 50
                    set par50 [string trim $xspec_tclout]

                    regsub -all { +} $par50 { } cpar50
                    set lpar50 [split $cpar50]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar50 0] 			---high53-rerror-Fe-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 50
                    set par50 [string trim $xspec_tclout]

                    regsub -all { +} $par50 { } cpar50
                    set lpar50 [split $cpar50]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar50 1] 			---high53-rerror-Fe+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 0] 			---high53-rerror-ejekta-norm-err" 
#--------------------------------------------------------------------------------------------------------	
                    tclout error 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 1] 			---high53-rerror-ejekta-norm+err \n"
#########################################################################################################
                    cpd /xw
                    plot ldat del
                    iplot
#########################################################################################################
            }   elseif {$param53 <2.9E+12} {
                    freeze 53

                    tclout param 53
                    set param53 [lindex $xspec_tclout 0]
                    if {$param53 ==1.00E+10} {
                            newpar 53 1.5E+11
                            newpar 38 0.50
                            fit
                            thaw 2,44-46,50,53
                            fit
                            freeze 53
                            thaw 38
                            fit
                            puts "Param53 (Tau_u) frozen now"
                    }   elseif {$param53 > 4.0E+13} {
                        newpar 53 2.5E+11
                            fit
                            thaw 2,44-46,50,53
                            fit
                            freeze 53
                            fit
                        puts "Param53 (Tau_u) frozen now"
                    }
                    thaw 2,44-46,50
                    fit
 #########################################################################################################                   
                    plot ldata del
                    tclout stat
                    set chi1 $xspec_tclout
                    tclout dof 
                    set dof1 [lindex $xspec_tclout 0]

                    setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
                    setplot command la f chi-squared $chi1 / $dof1 dof
                            

                    cpd $name$i-$m-$j-$z-d$loop
#########################################################################################                    
                    tclout stat
                    set stat [string trim $xspec_tclout]

                    regsub -all { +} $stat { } stat
                    set stat [split $stat]

                    puts $fileout "$i-$m-$j-$z [lindex $stat 0] 			---low53-chi-square"
#----------------------------------------------------------------------------------------		
                    tclout dof
                    set dof [string trim $xspec_tclout]

                    regsub -all { +} $dof { } dof
                    set dof [split $dof]
                    
                    puts $fileout "$i-$m-$j-$z  [lindex $dof 0] 				---low53-dof"
#----------------------------------------------------------------------------------------		
                    tclout param 2
                    set par2 [string trim $xspec_tclout]

                    regsub -all { +} $par2 { } cpar2
                    set lpar2 [split $cpar2]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar2 0] 			---low53-ism-nH"
#----------------------------------------------------------------------------------------		
                    tclout param 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 0] 			---low53-ism-norm"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 0] 			---low53-kT"
#--------------------------------------------------------------------------------------------------------
                    tclout param 43
                    set par43 [string trim $xspec_tclout]

                    regsub -all { +} $par43 { } cpar43
                    set lpar43 [split $cpar43]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar43 0] 			---low53-O"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 44
                    set par44 [string trim $xspec_tclout]

                    regsub -all { +} $par44 { } cpar44
                    set lpar44 [split $cpar44]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar44 0] 			---low53-Ne"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 45
                    set par45 [string trim $xspec_tclout]

                    regsub -all { +} $par45 { } cpar45
                    set lpar45 [split $cpar45]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar45 0] 			---low53-Mg"
#--------------------------------------------------------------------------------------------------------	
                    tclout param 46
                    set par46 [string trim $xspec_tclout]

                    regsub -all { +} $par46 { } cpar46
                    set lpar46 [split $cpar46]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar46 0] 			---low53-Si"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 50
                    set par50 [string trim $xspec_tclout]

                    regsub -all { +} $par50 { } cpar50
                    set lpar50 [split $cpar50]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar50 0] 			---low53-Fe"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 53
                    set par53 [string trim $xspec_tclout]

                    regsub -all { +} $par53 { } cpar53
                    set lpar53 [split $cpar53]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar53 0] 			---low53-Tau_u"
#-----------------------------------------------------------------------------------------------------	
                    tclout param 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 0] 			---low53-ejekta-norm \n" 
#########################################################################################################
                    parallel error 9
                    error max 50 2,37,38,43-46,50,55
#########################################################################################################                    
                    tclout stat 
                    set chi1 $xspec_tclout
                    tclout dof 
                    set dof1 [lindex $xspec_tclout 0]

                    setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
                    setplot command la f chi-squared $chi1 / $dof1 dof

                    plot ldata del
                    cpd $name$i-$m-$j-$z-e$loop
#----------------------------------------------------------------------------------------				
                    tclout stat
                    set stat [string trim $xspec_tclout]

                    regsub -all { +} $stat { } stat
                    set stat [split $stat]

                    puts $fileout "$i-$m-$j-$z  [lindex $stat 0] 			---low53-rerror-chi-square"
#----------------------------------------------------------------------------------------		
                    tclout dof
                    set dof [string trim $xspec_tclout]

                    regsub -all { +} $dof { } dof
                    set dof [split $dof]
                    
                    puts $fileout "$i-$m-$j-$z  [lindex $dof 0] 			 ---low53-rerror-dof"
#----------------------------------------------------------------------------------------
                    tclout error 2
                    set par2 [string trim $xspec_tclout]

                    regsub -all { +} $par2 { } cpar2
                    set lpar2 [split $cpar2]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar2 0] 			---low53-rerror-ism-nH-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 2
                    set par2 [string trim $xspec_tclout]

                    regsub -all { +} $par2 { } cpar2
                    set lpar2 [split $cpar2]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar2 1] 			---low53-rerror-ism-nH+err"
#--------------------------------------------------------------------------------------------------------
                    tclout error 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 0] 			---low53-rerror-ism-norm-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 1] 			---low53-rerror-ism-norm+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 0] 			---low53-rerror-kT-err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 1] 			---low53-rerror-kT+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 43
                    set par43 [string trim $xspec_tclout]

                    regsub -all { +} $par43 { } cpar43
                    set lpar43 [split $cpar43]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar43 0] 			---low53-rerror-O-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 43
                    set par43 [string trim $xspec_tclout]

                    regsub -all { +} $par43 { } cpar43
                    set lpar43 [split $cpar43]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar43 1] 			---low53-rerror-O+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 44
                    set par44 [string trim $xspec_tclout]

                    regsub -all { +} $par44 { } cpar44
                    set lpar44 [split $cpar44]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar44 0] 			---low53-rerror-Ne-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 44
                    set par44 [string trim $xspec_tclout]

                    regsub -all { +} $par44 { } cpar44
                    set lpar44 [split $cpar44]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar44 1] 			---low53-rerror-Ne+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 45
                    set par45 [string trim $xspec_tclout]

                    regsub -all { +} $par45 { } cpar45
                    set lpar45 [split $cpar45]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar45 0] 			---low53-rerror-Mg-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 45
                    set par45 [string trim $xspec_tclout]

                    regsub -all { +} $par45 { } cpar45
                    set lpar45 [split $cpar45]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar45 1] 			---low53-rerror-Mg+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 46
                    set par46 [string trim $xspec_tclout]

                    regsub -all { +} $par46 { } cpar46
                    set lpar46 [split $cpar46]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar46 0] 			---low53-rerror-Si-err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 46
                    set par46 [string trim $xspec_tclout]

                    regsub -all { +} $par46 { } cpar46
                    set lpar46 [split $cpar46]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar46 1] 			---low53-rerror-Si+err"
#--------------------------------------------------------------------------------------------------------			
                    tclout error 50
                    set par50 [string trim $xspec_tclout]

                    regsub -all { +} $par50 { } cpar50
                    set lpar50 [split $cpar50]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar50 0] 			---low53-rerror-Fe-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 50
                    set par50 [string trim $xspec_tclout]

                    regsub -all { +} $par50 { } cpar50
                    set lpar50 [split $cpar50]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar50 1] 			---low53-rerror-Fe+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 0] 			---low53-rerror-ejekta-norm-err" 
#--------------------------------------------------------------------------------------------------------	
                    tclout error 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 1] 			---low53-rerror-ejekta-norm+err \n"
#########################################################################################################     
                    freeze 2,43-46,50,
                    thaw 53
                    fit
#########################################################################################################
                    plot ldata del
                    cpd $name$i-$m-$j-$z-f$loop

                    tclout stat 
                    set chi1 $xspec_tclout
                    tclout dof 
                    set dof1 [lindex $xspec_tclout 0]

                    setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
                    setplot command la f chi-squared $chi1 / $dof1 dof

                    plot ldata del
                    cpd $name$i-$m-$j-$z-g$loop
#########################################################################################################      
                    tclout stat
                    set stat [string trim $xspec_tclout]

                    regsub -all { +} $stat { } stat
                    set stat [split $stat]

                    puts $fileout "$i-$m-$j-$z [lindex $stat 0] 			---low53-thaw-53-chi-square"
#----------------------------------------------------------------------------------------		
                    tclout dof
                    set dof [string trim $xspec_tclout]

                    regsub -all { +} $dof { } dof
                    set dof [split $dof]
                    
                    puts $fileout "$i-$m-$j-$z  [lindex $dof 0] 				---low53-thaw-53-dof"
#----------------------------------------------------------------------------------------		
                    tclout param 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar37 0] 			---low53-thaw-53-ism-norm"
#--------------------------------------------------------------------------------------------------------		
                    tclout param 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 0] 			---low53-thaw-53-kT"
#--------------------------------------------------------------------------------------------------------				
                    tclout param 53
                    set par53 [string trim $xspec_tclout]

                    regsub -all { +} $par53 { } cpar53
                    set lpar53 [split $cpar53]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar53 0] 			---low53-thaw-53-Tau_u"
#-----------------------------------------------------------------------------------------------------	
                    tclout param 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 0] 			---low53-thaw-53-ejekta-norm \n" 
#########################################################################################################
                    plot ldata del
                    cpd $name$i-$m-$j-$z-h$loop

                    tclout stat 
                    set chi1 $xspec_tclout
                    tclout dof 
                    set dof1 [lindex $xspec_tclout 0]

                    setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
                    setplot command la f chi-squared $chi1 / $dof1 dof

                    plot ldata del
                    cpd $name$i-$m-$j-$z-l$loop
#########################################################################################################	 
                    parallel error 4
                    error max 50 37,38,53,55
#----------------------------------------------------------------------------------------				
                    tclout stat
                    set stat [string trim $xspec_tclout]

                    regsub -all { +} $stat { } stat
                    set stat [split $stat]

                    puts $fileout "$i-$m-$j-$z  [lindex $stat 0] 			----low53-thaw-53-rerror-chi-square"
#----------------------------------------------------------------------------------------		
                    tclout dof
                    set dof [string trim $xspec_tclout]

                    regsub -all { +} $dof { } dof
                    set dof [split $dof]
                    
                    puts $fileout "$i-$m-$j-$z  [lindex $dof 0] 			 ----low53-thaw-53-rerror-dof"
#----------------------------------------------------------------------------------------
                    tclout error 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 0] 			----low53-thaw-53-rerror-ism-norm-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 37
                    set par37 [string trim $xspec_tclout]

                    regsub -all { +} $par37 { } cpar37
                    set lpar37 [split $cpar37]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar37 1] 			----low53-thaw-53-rerror-ism-norm+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 0] 			----low53-thaw-53-rerror-kT-err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 38
                    set par38 [string trim $xspec_tclout]

                    regsub -all { +} $par38 { } cpar38
                    set lpar38 [split $cpar38]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar38 1] 			----low53-thaw-53-rerror-kT+err"
#--------------------------------------------------------------------------------------------------------		
                    tclout error 53
                    set par53 [string trim $xspec_tclout]

                    regsub -all { +} $par53 { } cpar53
                    set lpar53 [split $cpar53]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar53 0] 			----low53-thaw-53-rerror-Tau_u-err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 53
                    set par53 [string trim $xspec_tclout]

                    regsub -all { +} $par53 { } cpar53
                    set lpar53 [split $cpar53]

                    puts $fileout "$i-$m-$j-$z [lindex $lpar53 1] 			----low53-thaw-53-rerror-Tau_u+err"
#--------------------------------------------------------------------------------------------------------	
                    tclout error 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 0] 			----low53-thaw-53-rerror-ejekta-norm-err" 
#--------------------------------------------------------------------------------------------------------	
                    tclout error 55
                    set par55 [string trim $xspec_tclout]

                    regsub -all { +} $par55 { } cpar55
                    set lpar55 [split $cpar55]

                    puts $fileout "$i-$m-$j-$z  [lindex $lpar55 1] 			----low53-thaw-53-rerror-ejekta-norm+err \n"
#########################################################################################################
                    plot ldata del
                    cpd $name$i-$m-$j-d$loop

                    tclout stat 
                    set chi1 $xspec_tclout
                    tclout dof 
                    set dof1 [lindex $xspec_tclout 0]

                    setplot command la t Model N63A spectrum: $i-$m-$j-$z$loop
                    setplot command la f chi-squared $chi1 / $dof1 dof

                    plot ldata del
                    cpd $name$i-$m-$j-$z-s$loop
#########################################################################################################
                    cpd /xw
                    plot ldat del
                    iplot                
######################################################################################################### 
                }
			data none
			model none
			close $fileout
#########################################################################################################
			}
			}
			}
			exit                                                
"""
#color 11 on 3
color 13 on 4
color 12 on 2
lwidth 8 on 4
lwidth 8 on 3
lwitdh 4.5 on 2
lwidth 4.5 on 1
lwidth 4.5 on 5
lwidth 4.5
csize 1.3
time off
LAbel 4 VP 0.165 0.85  "C18" csize 2
LAbel 1 VP 0.68 0.85 LIne 0 LStyle 4 MSize 1.5 CO 13 "Ejecta" csize 2
LAbel 3 VP 0.68 0.793 LIne 0 LStyle 4 MSize 1.5 CO 11 "CSM" csize 2
label pos y 2.5
la T
la F
plot


hardcopy C24.png/cps
quit

"""            