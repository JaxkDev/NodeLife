/*
*  __    __                  __            __        __   ______           
* |  \  |  \                |  \          |  \      |  \ /      \          
* | $$\ | $$  ______    ____| $$  ______  | $$       \$$|  $$$$$$\ ______  
* | $$$\| $$ /      \  /      $$ /      \ | $$      |  \| $$_  \$$/      \ 
* | $$$$\ $$|  $$$$$$\|  $$$$$$$|  $$$$$$\| $$      | $$| $$ \   |  $$$$$$\
* | $$\$$ $$| $$  | $$| $$  | $$| $$    $$| $$      | $$| $$$$   | $$    $$
* | $$ \$$$$| $$__/ $$| $$__| $$| $$$$$$$$| $$_____ | $$| $$     | $$$$$$$$
* | $$  \$$$ \$$    $$ \$$    $$ \$$     \| $$     \| $$| $$      \$$     \
*  \$$   \$$  \$$$$$$   \$$$$$$$  \$$$$$$$ \$$$$$$$$ \$$ \$$       \$$$$$$$
*   
* @author Jackthehack21                                                                    
*
*/

module.exports.execute = function(data){
    const os = require('os');
    
    const device = process.env.OS;
    const arm = process.env.PROCESSOR_ARCHITECTURE;
    const ver = os.release()

    // Check Device is Windows
    if(!(device === 'Windows_NT')){
        data.logger.critical(data.messages.incompatibleDevice);
        return false;
    }

    // Check Version is 10.x
    if(!(ver[0]+ver[1] === '10')){
        data.logger.critical(data.messages.incompatibleVersion);
        return false;
    }

    // Check Arm64 (not required but recommended)
    if(!(arm === 'AMD64')){
        data.logger.warn(data.messages.recommendedProcessorArchitecture);
    }

    return true;
}