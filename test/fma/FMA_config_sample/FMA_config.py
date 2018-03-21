import sys
import matplotlib.pyplot as plt

sys.path.append("../")
import sixdeskdb

params = {'legend.fontsize': 12,
          'figure.figsize': (12.5, 6.5),
         'axes.labelsize':  12,
         'axes.titlesize':  12,
         'xtick.labelsize': 12,
         'ytick.labelsize': 12,
         'image.cmap':'jet',
         'lines.linewidth':0.8,
         'lines.markersize': 5 }

plt.rcParams.update(params)

study = 'ats40_62.31_60.32'
db=sixdeskdb.SixDeskDB.from_dir('./studies/'+study+'/',include_fma_sixout=True)
for tunes in db.get_tunes():
  for seed in db.get_seeds():
    dirname=db.mk_analysis_dir(seed,tunes)
    plt.close('all')
    ##### FMA & configuration space
    turnse='e'+ str(db.env_var['turnse'])
    method_inputfile = db.get_db_fma_inputfile_method()
    
    fig, axes = plt.subplots(nrows=1, ncols=2)
    title = "This is a title"
    plt.suptitle(title)

    plt.sca(axes[0])
    db.plot_fma_scatter(seed,tunes,turnse,method_inputfile, var1 ='q1' ,var2 ='q2' ,dqlim=1e-1, plot_colorbar=False)
    db.plot_res_upto_order(15,c1 = 'darkgrey', c2='darkgrey')
    plt.xlim([0.2975, 0.315])
    plt.ylim([0.3075, 0.3250])
    plt.xlabel(r"$ \rm Q_x$")
    plt.ylabel(r"$\rm Q_y$")

    plt.sca(axes[1])
    db.plot_fma_scatter(seed,tunes,turnse,method_inputfile)
    plt.xlim([0.1,6.1]) 
    plt.ylim([0.1,6.1]) 
   
    plt.subplots_adjust(left=0.09, bottom=0.12, right=0.95, top=0.9, wspace=None, hspace=None)
    plot_name='test'
    plt.savefig('%s/%s.%s.%s.png'%(dirname,plot_name,turnse,method_inputfile[0][1]))
    plt.close('all')

    ##### Grid
    fig_grid, axes_grid = plt.subplots(figsize=(8,6))
    plt.sca(axes_grid)
    db.plot_fma_footprint(seed,tunes,turnse,method_inputfile[0][0],method_inputfile[0][1],grid=True,c_grid='b')
    plt.xlim([0.2975,0.3175])
    plt.ylim([0.3050,0.3250])
    plot_name='grid'
    plt.savefig('%s/%s.%s.%s.png'%(dirname,plot_name,turnse,method_inputfile[0][1]))
