import sh
import subprocess
import numpy as np
import pdb
import os
import copy

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
        print 'all files exist'
    elif np.any(file_list_exist):
        print 'some exist'
    else:
        print file_list
        print 'none exist'

    return file_list


if __name__=="__main__":
    
    exp_numbers_in=[19, 20, 21, 22, 25, 26, 27, 28]
                         
    file_list_created = create_list_of_files(start_experiment_name = 'annual_mean_ice_post_princeton_qflux_anoms_'+str(exp_numbers_in[0]),                    start_plot_name='ucomp_annual_mean_ice_post_princeton_qflux_anoms_'+str(exp_numbers_in[0])+'_timeseasons_250hPa',
                         start_number=exp_numbers_in[0],
                         exp_numbers=exp_numbers_in,
                         time_folder_name = '529_768',
                         base_folder = '/Users/sit204/mounts/gv3/sit204/plots',
                         control_exp_name = 'annual_mean_ice_post_princeton_qflux_control_1',
                         control_time_folder_name = '481_720')

    open_files_with_shell_script(file_list_created, program = 'acrobat')
    
    file_list_created = create_list_of_files(start_experiment_name = 'simple_continents_post_princeton_qflux_anoms_'+str(exp_numbers_in[0]),
                         start_plot_name='ucomp_simple_continents_post_princeton_qflux_anoms_'+str(exp_numbers_in[0])+'_timeseasons_250hPa',
                         start_number=exp_numbers_in[0],
                         exp_numbers=exp_numbers_in,
                         time_folder_name = '529_768',
                         base_folder = '/Users/sit204/mounts/gv3/sit204/plots',
                         control_exp_name = 'simple_continents_post_princeton_qflux_control_1',
                         control_time_folder_name = '481_720')

    open_files_with_shell_script(file_list_created, program = 'skim')