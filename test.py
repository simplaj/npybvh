import os

from bvh import Bvh


if __name__ == '__main__':
    anim = Bvh()
    anim.parse_file('pd_walk.bvh')
    
    # draw the skeleton in T-pose
    anim.plot_hierarchy()

    # extract single frame pose: axis0=joint, axis1=positionXYZ/rotationXYZ
    p, r = anim.frame_pose(0)

    # extract all poses: axis0=frame, axis1=joint, axis2=positionXYZ/rotationXYZ
    all_p, all_r = anim.all_frame_poses()

    # print all joints, their positions and orientations
    for _p, _r, _j in zip(p, r, anim.joint_names()):
        print(f"{_j}: p={_p}, r={_r}")

    # draw the skeleton for the given frame
    anim.plot_frame(22)

    # show full animation
    anim.plot_all_frames()
