import pm4py
from pm4py.objects.petri_net.utils import initial_marking, final_marking

log = pm4py.read_xes("ProcessMiningSampleLog.xes")
def eval(net, im, fm):
    eva =pm4py.fitness_alignments(log, net, im, fm)

    eva["precision"] = pm4py.precision_alignments(log, net, im, fm)

    eva["generelization"]=pm4py.algo.evaluation.generalization.algorithm.apply(log, net, im, fm)
    eva["simplicity"]=pm4py.algo.evaluation.simplicity.algorithm.apply(net)
    for x in eva.keys():
        print(x, eva[x])



def alpha_miner():
    net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(log)
    pm4py.view_petri_net(net, initial_marking, final_marking)
    gviz = pm4py.visualization.petri_net.visualizer.apply(net, initial_marking, final_marking)
    pm4py.visualization.petri_net.visualizer.view(gviz)
    pm4py.visualization.petri_net.visualizer.save(gviz, "alpha_petri_net.png")
    eval(net, initial_marking, final_marking)


def heuristic_miner():
    net= pm4py.discover_heuristics_net(log,dependency_threshold=0.5,and_threshold=0.65,loop_two_threshold=0.5)
    pm4py.view_heuristics_net(net)
    pm4py.save_vis_heuristics_net(net,"heuristic_net.png")

def heuristic_miner_petri():

    net, im, fm = pm4py.discover_petri_net_heuristics(log, dependency_threshold=0.5,and_threshold=0.65, loop_two_threshold=0.5)
    gviz = pm4py.visualization.petri_net.visualizer.apply(net, im, fm)
    pm4py.visualization.petri_net.visualizer.view(gviz)
    pm4py.visualization.petri_net.visualizer.save(gviz, "heuristic_petri_net.png")
    eval(net, im, fm)

if __name__ == '__main__':
    #alpha_miner()
    heuristic_miner()
    heuristic_miner_petri()