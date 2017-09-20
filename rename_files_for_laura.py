import os
import pdb

def get_new_plot_name(name_in):

    if 'flux_lhe_diff' in name_in:
        out_name = 'flux_lhe.pdf'

    if 'height_diff' in name_in and '_250hPa' in name_in:
        out_name = 'height_250.pdf'

    if 'omega_diff' in name_in and '_500hPa' in name_in:
        out_name = 'omega_500.pdf'

    if 'temp_diff' in name_in and '_925hPa' in name_in:
        out_name = 'temp_925.pdf'

    if 'ucomp_diff' in name_in and '_250hPa' in name_in:
        out_name = 'ucomp_250.pdf'        

    if 'flux_oceanq_diff' in name_in:
        out_name = 'ocean_qflux.pdf'

    if 'precipitation_diff' in name_in:
        out_name = 'precip.pdf'

    if 'slp_diff' in name_in:
        out_name = 'slp.pdf'
        
    if 't_surf_diff' in name_in:
        out_name = 't_surf.pdf'        
        
    return out_name

if __name__=="__main__":

    base_dir = '/Users/sit204/mounts/gv3/sit204/collab/laura_wilcox/second_set_of_isca_results_20_09_17/difference_plots/'
    
    folders = os.listdir(base_dir)
    
    for num_exp in range(1,len(folders)+1):
    
        old_name = folders[num_exp-1]
        new_name = 'anom_'+str(num_exp)+'_minus_control'
        
        if '_anoms_'+str(num_exp) in old_name:
            os.rename(base_dir+old_name, base_dir+new_name)
    
        contents_of_folder = os.listdir(base_dir+new_name)
        time_folders = [name for name in contents_of_folder if os.path.isdir(os.path.join(base_dir, new_name, name))]
        for time_folder in time_folders:
            plots = os.listdir(os.path.join(base_dir, new_name, time_folder))
            
            for plot in plots:
                new_plot_name = get_new_plot_name(plot)
                new_plot_path = os.path.join(base_dir, new_name, new_plot_name)
                if not os.path.isfile(new_plot_path):
                    os.rename(os.path.join(base_dir, new_name, time_folder, plot), new_plot_path)
            
            os.rmdir(os.path.join(base_dir, new_name, time_folder))
            
        