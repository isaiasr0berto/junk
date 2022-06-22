quick and easy package manager or qaepm

USE:

qaepm -option [param ...]

help [no args] show this list
update [no args]
fetch-pkg [pkg name, one only]
pull-pkg [pkg name, several allowed]
remove-pkg [pkg name, several allowed]
repair-pkg [pkg name, one only]

qaepm server struct..

root../ 
    /pkgs
        pkgs ...
        /pkgnamedir 
            pkginfo.json
            pkg.zip

{
    pkgName: "",
    pkgVersion: ""
    pkgModificationDate: "",
    pkgFile: "",
    pkgDescription: ""
    pkgGenre: ""
    pkgDeveloper: ""
    pkgYearCreation: ""
    pkgSiteUrl: ""
    pkgDevSiteUrl: ""
}

