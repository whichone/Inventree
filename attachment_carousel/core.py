"""An example part pnanel plugin that displays image attachments in a carousel"""

from plugin import InvenTreePlugin

from plugin.mixins import SettingsMixin#, UserInterfaceMixin

from . import PLUGIN_VERSION


#class AttachmentCarousel(SettingsMixin, UserInterfaceMixin, InvenTreePlugin):
class AttachmentCarousel(SettingsMixin, InvenTreePlugin):

    """AttachmentCarousel - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "Attachment Carousel"
    NAME = "AttachmentCarousel"
    SLUG = "attachment-carousel"
    DESCRIPTION = "An example part pnanel plugin that displays image attachments in a carousel"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "Jason Huang"
    WEBSITE = "https://my-project-url.com"
    LICENSE = "MIT"

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'

    
    
    
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    
    
    
    
    

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/ui/
    
    # Custom UI panels
    # def get_ui_panels(self, request, context: dict, **kwargs):
    #     """Return a list of custom panels to be rendered in the InvenTree user interface."""

    #     panels = []

    #     # Only display this panel for the 'part' target
    #     if context.get('target_model') == 'part':
    #         panels.append({
    #             'key': 'attachment-carousel-panel',
    #             'title': 'Attachment Carousel',
    #             'description': 'Custom panel description',
    #             'icon': 'ti:mood-smile:outline',
    #             'source': self.plugin_static_file('Panel.js:renderAttachmentCarouselPanel'),
    #             'context': {
    #                 # Provide additional context data to the panel
    #                 'settings': self.get_settings_dict(),
    #                 'foo': 'bar'
    #             }
    #         })
        
    #     return panels
    

    
