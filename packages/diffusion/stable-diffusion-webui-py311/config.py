
from jetson_containers import L4T_VERSION


package['build_args'] = {
    'STABLE_DIFFUSION_WEBUI_SHA': 'master',
    'STABLE_DIFFUSION_WEBUI_REF': 'refs/heads/master',
}