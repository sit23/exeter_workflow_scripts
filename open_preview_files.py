import sh
import subprocess
import numpy as np
import pdb
import os
import copy
import socket

def open_files_with_shell_script(files_list, program = 'preview'):

    full_file_string = ' '.join(files_list)

    if program == 'preview':
        return_value = subprocess.call('./prev_multiple '+full_file_string, shell=True)
    elif program == 'skim':
        return_value = subprocess.call('./skim_multiple '+full_file_string, shell=True)    
    else:
        return_value = subprocess.call('./acro_multiple '+full_file_string, shell=True)    
    
def create_list_of_files(start_experiment_name, start_plot_name, start_number, exp_numbers, time_folder_name, base_folder = '/Users/sit204/mounts/gv3/sit204/plots/', control_exp_name = None, control_time_folder_name = '481_720'):

    exp_name_prefix = start_experiment_name.replace('_'+str(start_number), '_')
    
#     exp_numbers = np.arange(start_number, end_number+1)
    
    exp_list = []
    file_list = []
    
    for exp in exp_numbers:
        exp_name = exp_name_prefix+str(exp)
        exp_list.append(exp_name)
    
        if control_exp_name is None:
            file_name = base_folder + '/exps/' + exp_name + '/' + time_folder_name + '/' + start_plot_name.replace('_'+str(start_number)+'_', '_'+str(exp)+'_') + '.pdf'
        else:
        
            diff_folder_name = exp_name + '_minus_'+control_exp_name
            diff_time_folder_name = time_folder_name + '_minus_' + control_time_folder_name
            
            document_name = start_plot_name.replace('_'+str(start_number)+'_', '_'+str(exp)+'_')
            
            final_document_name = document_name.replace('_'+exp_name, '_diff_'+exp_name+'_minus_'+control_exp_name)
            
            file_name = base_folder + '/diffs/' + diff_folder_name + '/' + diff_time_folder_name + '/' + final_document_name + '.pdf'            
            if not os.path.isfile(file_name):
                final_document_name = document_name.replace('_'+exp_list[0], '_diff_'+exp_name+'_minus_'+control_exp_name)
                file_name = base_folder + '/diffs/' + diff_folder_name + '/' + diff_time_folder_name + '/' + final_document_name + '.pdf'            
                   
        file_list.append(file_name)

    file_list_exist = copy.copy(file_list)

    for file_list_entry in file_list:
        file_list_exist[file_list.index(file_list_entry)] = os.path.isfile(file_list_entry)
        
    if np.all(file_list_exist):
        print('all files exist')
    elif np.any(file_list_exist):
        print('some exist')
    else:
        print(file_list)
        print('none exist')

    return file_list


if __name__=="__main__":
    
    hostname=socket.gethostname()
    
    if 'emps-thomson' in hostname:
        base_folder_use = '/Users/sit204/mounts/gv3/sit204/plots'
    elif hostname=='sitMacBookPro.local':
        base_folder_use = '/Volumes/gv3/sit204/plots/'        
    
#     exp_numbers_in=[21,22,25]    
#     exp_numbers_in=[13, 14, 15, 16, 22, 25, 26, 27, 28]
#     exp_numbers_in=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
#     exp_numbers_in=[13, 14, 15, 16, 17, 18]
#     exp_numbers_in = [17, 18, 23, 24]
#     exp_numbers_in=[1,2,3,7,8,9,29,30,31]
#     exp_numbers_in=[1,2,3,7,8,9]    
#     exp_numbers_in=[4,5,6, 10, 11, 12]    
    exp_numbers_in = list(range(19,23))
    
    var_to_plot_1='heat_budget_comparison_jja'
    time_str_1=''
    level_to_plot_1=''
    exp_name_1_anom = 'annual_mean_ice_post_princeton_qflux_anoms'
    exp_name_1_control = 'annual_mean_ice_post_princeton_qflux_control_1'

#     var_to_plot_2='heat_budget_comparison_jja'
#     time_str_2=''
#     level_to_plot_2=''
#     exp_name_2_anom = 'annual_mean_ice_post_princeton_qflux_anoms'
#     exp_name_2_control = 'annual_mean_ice_post_princeton_qflux_control_1'
    
#     var_to_plot='ucomp'
#     time_str='_timeseasons_'
#     level_to_plot='250hPa'

    try:
        var_to_plot_2
    except NameError:
        var_to_plot_2=var_to_plot_1
        time_str_2=time_str_1
        level_to_plot_2=level_to_plot_1 
        exp_name_2_anom = 'simple_continents_post_princeton_qflux_anoms'
        exp_name_2_control = 'simple_continents_post_princeton_qflux_control_1'          
                         
    file_list_created = create_list_of_files(start_experiment_name = exp_name_1_anom+'_'+str(exp_numbers_in[0]),                    start_plot_name=var_to_plot_1+'_'+exp_name_1_anom+'_'+str(exp_numbers_in[0])+time_str_1+level_to_plot_1,
                         start_number=exp_numbers_in[0],
                         exp_numbers=exp_numbers_in,
                         time_folder_name = '529_768',
                         base_folder = base_folder_use ,
                         control_exp_name = exp_name_1_control,
                         control_time_folder_name = '481_720')

    open_files_with_shell_script(file_list_created, program = 'acrobat')
    
    file_list_created = create_list_of_files(start_experiment_name = exp_name_2_anom+'_'+str(exp_numbers_in[0]),
                         start_plot_name=var_to_plot_2+'_'+exp_name_2_anom+'_'+str(exp_numbers_in[0])+time_str_2+level_to_plot_2,
                         start_number=exp_numbers_in[0],
                         exp_numbers=exp_numbers_in,
                         time_folder_name = '529_768',
                         base_folder = base_folder_use,
                         control_exp_name = exp_name_2_control ,
                         control_time_folder_name = '481_720')

    open_files_with_shell_script(file_list_created, program = 'skim')