from .mscmr import build


def build_dataset(image_set, args):
    if args.dataset == 'ACDC':
        return build(image_set, args)
    raise ValueError(f'dataset {args.dataset} not supported')
