import dataprovider.joint_dataprovider as joint_dataprovider
import model.joint_model as joint_model


def do_3_fold_cross_validation():
    dataset_path = "datasets/tmseg/data/sets/tfrecords/"

    sets = ["opm_set1", "opm_set2", "opm_set3"]

    runs = []

    for i in range(3):
        trainset = sets[:i] + sets[i + 1:]
        validationset = testset = sets[i:i + 1]

        dataprovider = joint_dataprovider.Dataprovider(path=dataset_path,
                                                       trainset=trainset,
                                                       validationset=validationset,
                                                       testset=testset)

        m = joint_model.Model(logdir="test/", dataprovider=dataprovider, should_step3=False)

        m.train()
        runs.append(m.inference())
    return runs