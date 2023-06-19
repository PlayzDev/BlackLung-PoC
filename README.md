# BlackLung-PoC
![GitHub all releases](https://img.shields.io/github/downloads/PlayzDev/BlackLung-PoC/total?style=flat-square&logo=GitHub&label=Downloads&link=https%3A%2F%2Fgithub.com%2FPlayzDev%2FBlackLung-PoC%2Freleases) ![GitHub release (release name instead of tag name)](https://img.shields.io/github/v/release/PlayzDev/BlackLung-PoC?style=flat-square&logo=GitHub) ![Static Badge](https://img.shields.io/badge/Python%20version%3A%20-%203.11.4%20-%230000FF?style=flat-square&logo=Python&label=Python%20version&color=%230000FF) ![Static Badge](https://img.shields.io/badge/Made%20in%20the%3A%20-%20United%20States%20%F0%9F%87%BA%F0%9F%87%B8%20-%20%230000FF?style=flat-square&label=Made%20in%20the%3A%20)




![BlackLung!](/Images/BlackLung-GitHub-Repo-Banner.png)


**BlackLung** is a windows based ransomware virus, and is fully written in python. I made BlackLung as a PoC (Proof of concept) to test the skills I have learned in the "Python programming for ethical hackers" course I am taking online. **BlackLung ransomware** has many features including a built in safeguard, which is enabled by default so you don't accidentally encrypt the files on your main system. However, you can disable the safeguard if you want to.

 **(PLEASE NOTE):** that the server script (Which is the server that the BlackLung ransomware sends the key and other info to), **IS NOT**  publicly available/accessible due to any potential legal issues.  

** **

## DISCLAIMER: ##
                                                                                                                                                                               
**BlackLung Ransomware is just a POC  (Proof of concept) ransomware virus, and it's code is strictly for educational purposes only!**  
**Any illegal use of BlackLung Ransomware or it's source code is strictly prohibited and will result in the source code for Blacklung Ransomware being removed from the public domain and all public access to it's source code, Wiki's, and Github page will be revoked permanently!.**  

**Please note that even though I have already created the server script (which the server that the ransomware sends the key, and the hostname, and the date and time of the victim's computer to), I WILL NOT be making it publicly available/accessible due to legal reasons/potential legal issues.**  



## WARNING: 
**Since the server script is not publicly available, once you run BlackLung THERE IS ABSOLUTELY NO WAY TO GET YOUR FILES BACK!!! You have been warned!!!**  

** **

<br>

## Table of contents:



1. [Features of _BlackLung_ ransomware](https://github.com/PlayzDev/BlackLung-PoC#features)
1. [Cloning the repository](https://github.com/PlayzDev/BlackLung-PoC/edit/main/README.md#cloning-the-repository)
2. Installing the required dependencies
3. Disabling the safeguard
4. Compiling into a stand-alone executable



** ** 

<br>
<br>



## Features:


###### Features of BlackLung ransomware:

1. Safeguard to protect against accidental encryption - (Enabled by default)
1. Generates a random key every time BlackLung ransomware is run
2. Grabs the hostname of victim's machine
3. Grabs the current date and time of the victim's machine
4. Sends the key, hostname, and the date and time of the victim's PC to a server - (Disabled by default - server script not publicly available).
5. Encrypts all the files on the C: drive

<br?

While there are quite a few features in **_BlackLung-PoC_**, there is no publicly available server script which is needed to run the server that the BlackLung ransomware sends the key and hostname to. As for _"when"_ the server script will be made publicly available, the answer unfortunately is **_NEVER_**. And the reason for that as I have mentioned above is due to any potential legal issues, as well as potential legal concerns.

** **

<br>
<br>

   
## Cloning the repository:

<br>

###### Copy and paste the following into your terminal or command prompt, to clone the repository for _BlackLung_ ransomware:

```git
git clone https://github.com/PlayzDev/BlackLung-PoC.git
```

<br>
<br>

** **


