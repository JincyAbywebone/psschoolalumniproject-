from .models import Staff
from .models import ModuleSettings  


def staff_context(request):
    """
    Adds 'staff' object for the currently logged-in user (if exists)
    """
    try:
        if hasattr(request, "user") and request.user.is_authenticated:
            staff = Staff.objects.filter(admin=request.user).first()
            return {"staff": staff}
        return {}
    except Exception:
        return {}

def module_settings_context(request):
    """
    Make 'modulesettings' available in all templates automatically.
    """
    if request.user.is_authenticated:
        # Only fetch module settings for logged-in users
        modulesettings = ModuleSettings.objects.all()
    else:
        modulesettings = []
    
    return {'modulesettings': modulesettings}


def session_context(request):
    """
    Adds 'current_session' from the database for all templates.
    """
    try:
        from .models import Session
        current_session = Session.objects.last()
        return {'current_session': current_session}
    except Exception:
        return {}        