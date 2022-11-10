# Installers

Installation (or setup) of a computer program (including device drivers and plugins) is the act of making the program ready for execution. Installation refers to the particular configuration of a software or hardware with a view to making it usable with the computer. A soft or digital copy of the piece of software (program) is needed to install it. There are different processes of installing a piece of software. Because the process varies for each program and each computer, programs (including operating systems) often come with an installer, which is a specialised program responsible for doing whatever is needed (see below) for the installation. Installation may be part of a larger software deployment process.

Installation typically involves code (program) being copied/generated from the installation files to new files on the local computer for easier access by the operating system, creating necessary directories, registering environment variables, providing separate program for un-installation etc. Because code is generally copied/generated in multiple locations, uninstallation usually involves more than just erasing the program folder. For example, registry files and other system code may need to be modified or deleted for a complete uninstallation.

# Example Installation

Let us take an example of what is happening by installing the [Intel oneAPI runtime](https://www.intel.com/content/www/us/en/developer/articles/tool/compilers-redistributable-libraries-by-version.html). Downloading the 2022 version we obtain the file `w_dpcpp_cpp_runtime_p_2022.2.0.9553.exe`. Running this will perform an installation process as shown below.

![](./images/intel_oneAPI.PNG)

Performing the installation process, the first thing might be to notice that we now have additional **environment variable**. Under System Variables, the key has the value of `INTEL_DEV_REDIST` and the value is `C:\Program Files (x86)\Common Files\Intel\Shared Libraries\`. Now, looking inside this directory we can find all of the files that were extracted and moved here during the installation process. This process only needs to be once and is shared, meaning other software will not reinstall the runtime again and instead simply check for the existing environment variable, therefore saving space.

![](./images/intel_oneAPI_installed.PNG)

# Building Software

When creating software and shipping it to users, the executeable (`w_dpcpp_cpp_runtime_p_2022.2.0.9553.exe`) is included and typically installed from configurations setup by an installer. One example installer could be [inno setup](https://jrsoftware.org/isinfo.php). It is our responsibility to correctly configuration it so that the executeable is ran so that the user has the correct files to execute to main software.

# Programming Utilization

When running from source, it is necessary to access the runtime redistributables. However, when running from source code instead of executing a `.exe` the build and installation process is not done for you to immediately find and utilize the necessary files. Therefore, the files must be correctly added to the path. For example, when writing software in Python, if my software required the intel oneAPI redistributables previously installed to find and utilize them when running from source they must be added to the environment path. A "path" are a series of directories where our software will search for files.

A very simplified example, with no error handling can be shown as;

```python
intel_runtime = os.environ.get('INTEL_DEV_REDIST') # System Variable
intel_runtime = os.path.join(os.path.normpath(intel_runtime), 'intel64')
os_path = os.environ['PATH'].split(os.pathsep)
os_path.insert(0, intel_runtime)
os.add_dll_directory(intel_runtime)
os.environ['PATH'] = os.pathsep.join(os_path)

```
