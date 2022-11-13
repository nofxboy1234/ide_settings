Windows update

Nvidia graphics driver update
FloTP
	Unreal Engine
		*Jetbrains Rider
			*Logic Driver Pro
			*DragonIK

			Darker Nodes
			Electronic Nodes
######################################



FloodThePalaces Setup:
- UE 4.26.1
Microsoft Visual Studio Community 2019
	- MSBuild
	- .NET Framework 4.5 targeting pack
	- .NET Framework 4.6.2 targeting pack
	- .NET Framework 4.8 SDK
	- .NET Framework 4.8 targeting pack
- Rider for Unreal 2020.3.4


######################################
When starting a new UE project:
	# Open .sln with Rider
	# Let Rider install RiderLink into Engine 
	# 	(happens once e.g. "Engine/Plugins/Developer/RiderLink")
	# In UE4Editor, activate RiderLink plugin
	# Check that there's 2 Rider* plugins
	# Set Rider as Source editor

# To make sure project is fresh
Delete:
	.idea
	.vs
	Binaries
	Intermediate
	.sln
	# ~Saved
	# ~Build
Rt click .uproject -> Generate Visual Studio Project Files
Open Rider -> Open project .sln
Clean Project
Build Project
Close Rider -> Open project .sln

Open UE4 from Rider
Make code change
Build Project->UE4 Hot Reloads (with sound)
######################################






######################################
Rider Shortcuts:

shift+shift
alt+enter

toggle zen mode: alt+z

Rider panel shortcuts:
Alt+0: Build
Alt+1: Explorer
Alt+2: TODO
Alt+3: Find
Alt+4: Commit
Alt+8: Unreal
Alt+9: Git
show text editor window(code): esc

open any symbol: shift+shift
quick actions/refactoring: alt+enter

Alt+Y: Navigate to class
toggle between header and code: alt+o
goto declaration/definition: (alt+`, enter)
bookmarks: ctrl+k+k, ctrl+`

Navigate file member: alt+m
(alt+m again to Include members from related files):
This lists base class symbols.
If you type a word that matches part of a base class symbol, it also
shows, even when this is unticked. 

alt+home: Go to Super method/class

go back/forward: alt+left
				 alt+right

rename: ctrl+r,r

autocomplete: ctrl+space

show arguments in brackets: ctrl+shift+space

Select function signature: ctrl+shift+space||p

Delete line: ctrl+shift+l

close tab: ctrl+f4

alt+up: previous method
alt+down: next method

toggle comment line: ctrl+/

Show quick documentation: alt+q
Show error tooltip/info: ctrl+7

alt+pg up/down: go to next/prev err

Insert line before: ctrl+enter
Insert line after: shift+enter
Complete Statement: ctrl+shift+enter (e.g. Put ; at end of line)


Navigate, Type Hierarchy: Ctrl+E, H

move line up: ctrl+shift+up
move line down: ctrl+shift+down


Navigate to:
	Derived Symbols: alt+G
	Show Usages of Symbol: alt+H (usages shown in dropdown)
	Find Usages of Symbol: shift+f12 (list usages in panel)
	Type of Symbol: alt+t




********************************************

********************************************
UE4 tips:
In edit mode:
p: Show AI navigation
g: Show ui overlays

In play mode:
~
stat fps
show collision
r.vsync 1
t.maxFPS 60

Starting Settings:
Set project view to "Columns"
Hide Output Log as it can slow editor down
Tick "Show fps" in viewer dropdown
Editor Preferences->
	Appearance->
		Asset Editor Open Location = Main Window
	Play->
		Game Gets Mouse Control = True
Project Settings->
	Maps & Modes->
		Default Game Mode
		Editor Startup Map
		Game Default Map
	Input->
	Rendering->
		Bloom = False
		Auto Exposure = False
		Motion Blur = False
		Ray Tracing = False

Project Settings->Rendering->Ray Tracing->Turn on and off to check effect on framerate.


Checking if key/button is held down:
	PlayerController.IsInputKeyDown(FKey key) const;
	Source for above from Unreal Engine Developer:
		https://forums.unrealengine.com/development-discussion/blueprint-visual-scripting/533-input-held-down?p=135280#post135280

If a variable is removed from a c++ class -> Press "Compile" in UE to refresh BP class
If adding a variable to a c++ class -> UE seems to refresh it automatically		
Changing values in constuctor methods, or at initialization in header file, crashes UE editor,
so close Editor if doing this.

********************************************
Clean project: ctrl+shift+f6
Build project: ctrl+shift+f7
Run UE4 without debug: ctrl+f5

# Play game: ctrl+p
# Stop game: ctrl+i
Stop UE4 without debug: shift+f5

********************************************



-- To remove a plugin in unreal
#############################################
Remove references+variables in code that use plugin.
Delete files+classes (from win explorer)+BP in project that use plugin.

Delete:
	# .idea
	.vs
	Binaries
	Intermediate
	.sln
	~Saved
	~Build
Rt click .uproject -> Generate Visual Studio Project Files
Open Rider -> Open project .sln
Clean Project
Build Project
Close Rider -> Open project .sln

- At this point, plugin is not used in project, but still enabled.

Open project in unreal
Re-compile any BP that referenced the plugin as variables etc
Run to test


Disable plugin in project
Remove project from .build.cs and ~uproject

Delete:
	# .idea
	.vs
	Binaries
	Intermediate
	.sln
	~Saved
	~Build
Rt click .uproject -> Generate Visual Studio Project Files
Open Rider -> Open project .sln
Clean Project
Build Project
Close Rider -> Open project .sln

Uninstall plugin from engine using launcher

Delete:
	# .idea
	.vs
	Binaries
	Intermediate
	.sln
	~Saved
	~Build
Rt click .uproject -> Generate Visual Studio Project Files
Open Rider -> Open project .sln
Clean Project
Build Project
Close Rider -> Open project .sln

Package project to test
#############################################

Freshly setting up Preferences in UE4 after clearing all the above "Delete:" files:
	- Connect to Source Control
	- Show Sources (Asset Browset panel)
	- View options -> list
	- Play, advanced settings, Game gets mouse control = True
	- Project Settings, Rendering -> turn off Auto Exposure and Motion Blur
	- Output Log -> Settings -> Clear on PIE

	- Editor Preferences, Appearance, Asset Editor Open Location = Main Window
	                     - Plugins, Darker Nodes Plugin
	                     	- Blueprint regular node radius = 0
	                     	- Blueprint var node radius = 0
	                     	- Blueprint node header opacity = 0.5
	                     	- Extend nodes = True
	                     - Plugins, Electronic Nodes
	                     	- Wire Style = Subway
	                     	# - Force draw bubbles = True
	                     	# - Round radius = 5
	                     	# - Activate Ribbon = True


