import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile76690Navigator from '../features/UserProfile76690/navigator';
import Maps76671Navigator from '../features/Maps76671/navigator';
import Settings76649Navigator from '../features/Settings76649/navigator';
import Settings76634Navigator from '../features/Settings76634/navigator';
import NotificationList76633Navigator from '../features/NotificationList76633/navigator';
import Maps76632Navigator from '../features/Maps76632/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {
    SplashScreen: {
      screen: SplashScreen
    },
    //@BlueprintNavigationInsertion
UserProfile76690: { screen: UserProfile76690Navigator },
Maps76671: { screen: Maps76671Navigator },
Settings76649: { screen: Settings76649Navigator },
Settings76634: { screen: Settings76634Navigator },
NotificationList76633: { screen: NotificationList76633Navigator },
Maps76632: { screen: Maps76632Navigator },

    /** new navigators can be added here */
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu,
    initialRouteName: 'SplashScreen',
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
